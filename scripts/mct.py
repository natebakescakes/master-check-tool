import sys
import os
import tkinter
import datetime
from optparse import OptionParser
from tkinter import filedialog

import xlrd
import xlsxwriter
import pandas as pd

from master_check import master_check
import crosscheck

SHEET_NAMES = [
    'TNM_IMP_BUILDOUT',
    'TNM_CONTAINER_GROUP',
    'TNM_IMP_CUSTOMER_CONTRACT',
    'TNM_IMP_CUSTOMER_CONTRACT_DETAI',
    'TNM_CUSTOMER_PARTS_MASTER',
    'TNM_INNER_PACKING_BOM',
    'TNM_MODULE_GROUP',
    'TNM_PARTS_MASTER',
    'TNM_SHIPPING_CALENDAR',
    'TNM_EXP_SUPPLIER_CONTRACT',
    'TNM_SUPPLIER_PARTS_MASTER',
    'TNM_TTC_CONTRACT'
]

master_files = {}
path = ""

def open_dialog():
    tkinter.Tk().withdraw() # Close the root window
    in_path = filedialog.askdirectory() # Choose folder
    return in_path

def results_filename():
    case_no = os.path.basename(path)[:12] # Get case_no
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # time serial

    return 'mctresults_%s-%s.xlsx' % (case_no, timestamp)

def results_format(writer):
    # FAIL - Light red fill with dark red text
    format_fail = writer.book.add_format( {'bg_color': '#FFC7CE', 'font_color': '#9C0006'} )

    # PASS - Green fill with dark green text
    format_pass = writer.book.add_format( {'bg_color': '#C6EFCE', 'font_color': '#006100'} )

    # WARNING - Yellow fill with dark yellow text
    format_warning = writer.book.add_format( {'bg_color': '#FFEB9C', 'font_color': '#9C6500'} )

    # Text Alignment - Left
    format_text_left = writer.book.add_format( {'align': 'left', 'valign': 'vcenter'} )

    # Text Wrap, verticle alignment = centre
    format_general = writer.book.add_format()
    format_general.set_text_wrap()

    # Iterate through all sheets for uniform formatting
    for sheet in writer.book.worksheets():
        sheet_to_format = sheet
        sheet_to_format.set_zoom(85)

        # Column width and text alignment
        sheet_to_format.set_column('A:A', 4.50, format_text_left)
        sheet_to_format.set_column('B:B', 10.00, format_text_left)
        sheet_to_format.set_column('C:C', 23.00, format_text_left)
        sheet_to_format.set_column('D:D', 16.00, format_text_left)
        sheet_to_format.set_column('E:E', 16.00, format_text_left)
        sheet_to_format.set_column('F:F', 9.50, format_text_left)
        sheet_to_format.set_column('G:G', 23.00, format_text_left)
        sheet_to_format.set_column('H:H', 23.00, format_text_left)
        sheet_to_format.set_column('I:I', 91.00, format_text_left)

        # text wrap
        sheet_to_format.set_column('I:I', 91.00, format_general)

        # Conditional Formatting
        sheet_to_format.conditional_format('F2:F1048576', {'type': 'cell', 'criteria': '==', 'value': '"PASS"', 'format': format_pass})
        sheet_to_format.conditional_format('F2:F1048576', {'type': 'cell', 'criteria': '==', 'value': '"FAIL"', 'format': format_fail})
        sheet_to_format.conditional_format('F2:F1048576', {'type': 'cell', 'criteria': '==', 'value': '"WARNING"', 'format': format_warning})

        # Freeze Panes
        sheet_to_format.freeze_panes(1, 1)

    return writer

# Automatic checking of all worksheets:
if __name__ == "__main__":

    parser = OptionParser()
    parser.set_defaults(check_single=False, crosscheck=False)
    parser.add_option("-s", "--single",
                      action="store_true", dest="check_single", default=False,
                      help="Check a single master sheet, default is all sheets")
    parser.add_option("-c", "--crosscheck",
                      action="store_true", dest="crosscheck", default=False,
                      help="Compare latest submitted MRS with Temp folder")
    parser.add_option("-o", "--open", dest="QADB_no",
                      help="Specify QADB code to search", metavar="QADB")

    (options, args) = parser.parse_args()

    # If QADB_no not specified
    if options.QADB_no == None:
        path = open_dialog()

        if path == '':
            print ('You haven\'t selected a file.')
            os.system('pause')
            sys.exit()
    else:
        pass

    if len(os.listdir(os.path.join(path, '1) Submit'))) == 0:
        print ('The folder \'1) Submit\' is empty!')
    else:
        for i, filename in enumerate(os.listdir(os.path.join(path, '1) Submit'))):
            if filename.lower().endswith('.xls'):
                try:
                    print ('%d: %s' % (i, filename))
                except UnicodeEncodeError:
                    print ('%d: [Filename contains non-ASCII characters]' % i)

        index = input('Enter index of file you wish to access: ')
        master_files['xl_workbook'] = xlrd.open_workbook(os.path.join(path, '1) Submit', os.listdir(os.path.join(path, '1) Submit'))[int(index)]), formatting_info=True)

        # Check whether valid sheet name input
        for sheet_name in master_files['xl_workbook'].sheet_names():
            if sheet_name in SHEET_NAMES:
                pass
            else:
                print ('%s is not a valid sheet name. Please modify it before running again.' % sheet_name)
                os.system('pause')
                sys.exit()

        if options.crosscheck:
            if crosscheck.crosscheck(master_files['xl_workbook'], os.path.join(path, '5) Temp')):
                print ('Temp File OK')
            else:
                print ('Temp File FAIL')
            os.system('pause')
            sys.exit()

        if not options.check_single:
            writer = pd.ExcelWriter(os.path.join(path, results_filename()), engine = 'xlsxwriter')

            for i, sheet in enumerate(master_files['xl_workbook'].sheets()):
                master_files['xl_sheet_main'] = master_files['xl_workbook'].sheet_by_index(i)

                if master_files['xl_sheet_main'].cell_value(2, 0) != '':
                    master_type = master_files['xl_sheet_main'].cell_value(2, 0)
                elif master_files['xl_sheet_main'].cell_value(1, 0) != '':
                    master_type = master_files['xl_sheet_main'].cell_value(1, 0)
                else:
                    print ('MRS Header is blank, please check MRS')
                    os.system('pause')
                    sys.exit()

                print ('Checking %s' % master_type)

                df = master_check(master_type, master_files, path)

                # Increment row value by 1 to align with excel rows
                if df is not None:
                    df['Row'] += 1
                else:
                    print ('Something went wrong with the master check module')
                    os.system('pause')
                    sys.exit()

                # Modify label of CCD
                if master_type == 'Customer Contract Parts Master':
                    master_type = 'Customer Contract Details'

                sequence = ['NEW/MOD', 'Field', 'Primary Key', 'Primary Key (Alt)', 'Results', 'Submitted', 'Reference', 'Reason'][:]
                df.set_index('Row', inplace=True)
                display_df = df[sequence]
                display_df.to_excel(writer, sheet_name=master_type.upper(), engine='xlsxwriter')

            writer = results_format(writer)

            writer.save()

        else:
            # Open the workbook and retrieve worksheets
            print ('Retrieved worksheets:')
            for i, sheet in enumerate(master_files['xl_workbook'].sheets()):
                print ('%d: %s' % (i, sheet.name))

            # Worksheet selector
            index = input('Enter index of sheet you wish to check: ')
            master_files['xl_sheet_main'] = master_files['xl_workbook'].sheet_by_index(int(index))
            print('You have selected sheet: %s' % xl_sheet.name)

        print ('Master Check Complete')
        os.system('pause')
        sys.exit()
