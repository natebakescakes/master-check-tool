# Change Log
All notable changes to this project will be documented in this file.

## [1.1.2] - TBA
### Added
- Added Module Group Code check to see if it is in sequential order
- Added check in revive parts to check whether TTC Contract No. has been discontinued
- Added check in Buildout Master to check whether Customer Contract Detail has been discontinued
- Added new WEST data for PH and VN

### Changed
- Changed Build-out master discontinued parts check comment.
- Added strip() to all Customer Contract Details: Supplier Delivery Pattern checks
- Added warning to Customer Contract Details: Discontinue check to manually check for pending orders

### Fixed
- Parts Master: Discontinued check considers submitted customer contract details
- Customer Parts Master: Discontinued check considers submitted customer contract details
- Buildout Parts Master: Discontinued check considers submitted customer contract details
- Fixed Exprt/Middle WEST Check error message for TTC Contract Master
- Customer Contract Details Master: Multiple Customer Contract check considers discontinued parts
- Module Group Master: TTC Contract check considers discontinued parts
- Updated RU Office Master

## [1.1.1] - 2016-11-18
### Added
- Added Submitted MRS vs Temp Folder check, use --crosscheck flag (currently only checks values)
- Added check in Customer Contract Details/Customer Parts Master to check Customer Parts Name for non-ascii characters
- Added check in Supplier Parts Master to check Supplier Parts Name for non-ascii characters
- New payment terms registered (SC2016090025)
- Add new Suppliers (TBSJ3, TBSJ4) that require Supplier Back No.
- Added check to flag out Parts Master: Display Parts No. with no hyphen at all

### Changed
- Removed pre-SRBQ Apply Date and Non-English Supplier Parts Name support
- Changed Customer Parts Master: IP Specs Apply Date check to feedback warning for <MRS Upload Date>
- Customer Parts Master: Orderlot Apply Date will now prompt warning if 1st of current month
- Changed wording of Customer Contract Details: Supplier Code check
- Account for possibility that TTC Contract/Module Group check will not have any active parts
- Account for Exp WH Code when checking Module Type
- No need to check Display Parts No. format if JP-sourcing
- Re-did TTC Contract: Imp Consignee check
- Added format check for Customer Parts: IP Specs check
- Changed error message for GM issues

### Fixed
- Fixed Customer Contract Details: Customer Contract 3 check issue status
- IP Gross Weight, Parts Net Weight check, fix floating point issue
- Catch Customer Parts Master: Imp HS Code ValueError
- Fix check for Module Group Master: Customer Condition interaction with IN region
- Fix error in Customer Contract Details: Model BOM check
- TTC Contract: Shipping Route check now properly considers only non-discontinued parts
- Cleaned up Model BOM reference in Customer Contract Details: Discontinue check
- Cleaned up Customer Contract: WEST check, fix error
- Fixed error message of Container Group: Destination Port check
- Fixed Customer Contract Details: Duplicate Part check
- Enabled Customer Contract Details: Customer Part Name check 1
- IP Specs Apply Date properly checked when IP Specs is being modded

## [1.1] - 2016-05-27
### Added
- New payment terms registered (SC2016010161)
- Added check in revive parts to check whether Customer Contract No. has been discontinued
- Added check in Customer Contract Details to check whether Supplier Parts have been registered
- Added discontinue check in TTC Parts Master
- Added Customer Contract Details: Discontinued Contract check for all 'NEW' and 'MOD' rows
- **ARS S-0125**: Added Customer Contract: Imp WH No Unpack Flag checks
- **ARS S-0125**: Customer Contract Details: Imp WH No Unpack Flag checks
- Add Module Group, TTC Contract checks to Revive check
- New payment terms registered (SC2016030170)

### Changed
- Restructured all Master Data into its own master_data package
- Removed requirement to have IMS_Currency and IMS_Payment_Terms in Backup
    - Now function as static assets in master_data
- Changed output filename to "mctresults_[case_no]-[timestamp].xlsx"
- Updated TTC Contract: Customer Inventory Flag check with ARS B-0086 change
- Changed algorithm for Customer Contract Details duplicate check
- Updated Customer Contract Details to include S-0125 check
- Changed Customer Parts: West Customer No. to reference Imp Country field

### Fixed
- Fixed Supplier Parts Master: Box Specs/M3 typecast error
- Cleanup TTC Parts: WEST Field check
- **BUGFIX #5** - Fixed false positive in Customer Contract Details: Customer Contract check
- Fixed error in Build-out master that caused program to crash
- Minor typecasting fixes in Supplier Parts & Customer Parts
- Fixed dependencies on Supplier Parts Master
- Module Group Code should have 1 TTC Contract check now only considers discontinued parts
- Customer Contract Details: Revive check now considers discontinuing parts in same submitted master
- Module Group Master: Module Type check now only considers non-discontinued entries
- Fixed error in Customer Parts Master: Inner Packing Time check that caused program to crash
- Customer/Supplier Parts: Discontinued check now considers multiple contracts
- Fixed Inner Packing BOM: MOD check that caused program to check
- Cleaned up Customer Contract Details: Module Group check 3 to use correct algorithm
- Fixed wrong variable in Customer Parts: MOD check
- Fixed casting issue in Parts Master: Net Weight check
- Fixed variable typo in Parts Master: WEST fields check that caused program to crash
- Proper error handling for Build-Out Master: Date check
- Added warning for MOD reference check for blank cells but filled in system
- Fixed Customer Contract: Cross-dock check that caused program to crash
- Fixed Container Group: Discontinue check that caused program to crash
- Fixed Customer Contract Details: TTC Contract check 3 to account for discontinuing parts
- Fixed Container Group: Destination, Source Port check to account for discontinuing parts
- Fixed Customer Contract: Discontinue check that caused program to crash
- Updated Customer Contract Details: Customer Contract check to consider false positives
- Updated Customer Contract Details: No Unpack Flag check to consider changes in Module Group Master
- Fixed Inner Packing BOM: SPQ check that caused program to crash

## [1.0.3b] - 2016-01-19
### Added
- Added extra logic in Supplier Contract: WH Code check to see if WH Code already registered before
- Moved pre-ARS and 'Check All Master Sheets?' to option flags
    - Run program on command line with '-h' or '--help' flag to see list of options
- **HotFix**: Recompiled into .exe

### Fixed
- Fixed false positive in Module Group Code check for IN codes
- **BUGFIX #4** - Rewrote Module Group: Shipping Frequency check to be more accurate
    - Rewrote all Shipping Frequency checks for robustness
- **BUGFIX #2** - Fixed false positives in TTC Parts: Material Tax Class
- Added GM check for MOD West fields
- Added Gross Weight check for MOD Customer Parts: Next_SPQ

## [1.0.3] - 2016-01-13
### Added
- Added ability to reference .xlsx for Global Master check
- Added ability to reference post-update GM in Results Folder (only .xlsx)
- Added extra logic to discern between S500 and non-S500 if there is discrepancy in GM data
- Added check if 'NEW/MOD' fields have values aside from 'NEW' and 'MOD' (includes whitespace)
- Added Supplier Code and Exp Country reference for Customer Parts Master: Exp Back No. check
- Added additional information for NEW entries that are already registered in System
- Added 'Null' to list of Exp Back No. in Customer Parts Master: Exp Back No. check to skip check
- Added extra logic in Container Group: WH Code check to see if WH Code already registered before
- Added extra check for MOD Customer/Supplier Parts - Raise error if part has already been discontinued
- Added extra logic in Container Group: Container Type check to see if Container Type already registered before
- Added extra logic in Module Group: WH Code check to see if WH Code already registered before
- Added extra logic in Part Master: WEST Fields to consider multiple Imp/Exp Country scenario

### Fixed
- Fixed error in Customer Parts: Imp HS Code logic to show PASS for <same as exp>
- Strip whitespace from 'NEW/MOD' fields for more accurate classification of rows
- Fixed error in Customer Contract Details: Module Group that caused program to crash occasionally
- Fixed error that causes non-ASCII filenames to crash program
- Fixed false positives in Parts Master: WEST Fields (Exp) for C1 parts.
- Fixed false negative in Customer/Supplier Parts Master: Parts Master WEST check for WESt-optional TW parts
- Fixed error in Customer Contract: Cross Dock Flag referencing the wrong cell, causing program to crash
- Fixed error in TTC Contract: WEST Exp Sales No./Imp Purchase No. that caused program to crash
- Fixed error in Customer Contract Details: TTC Contract check for PK parts that caused program to crash
- Fixed false positives in TTC Contract: Mid E-Signature Flag
- Fixed errors in all Shipping Route checks, causing first row to not be referenced.
- Fixed errors in Compulsory Field check that caused program to crash
- Fixed syntax error in Module Group Master: Module Type check that caused program to crash
- Rewrote Customer Contract Details: TTC Contract check for Module Groups
- Fixed error in Container Group: Source Port/Destination Port check
- Fixed false positive in Supplier Parts Master: TTC Parts No. check for part in Customer Contract Details

## [1.0.2] - 2015-12-22
### Added
- Added additional checkpoint for Customer Contract Details: Customer Parts Name to tally with Customer Parts Master
- Added 'Press any key to exit' to prevent auto-close of command line
- Added additional checkpoint for Customer Parts Master: Paired Parts (Show error for if TTC P/N Paired Parts different OL from Customer Part)
- Added additional checkpoint for Customer Parts Master: Part No. (Show error if no WEST Field registered for Imp WEST Customer in Parts Master)
- Added additional checkpoint for Supplier Parts Master: Part No. (Show error if no WEST Field registered for Exp WEST Supplier in Parts Master)
- Added additional Suppliers (TH-TBJ1 and TH-TBSJ2) that require Back No. check in Supplier Parts Master

### Changed
- Rewrote logic for Customer Contract Details: Supplier Contract to be more robust
- Rewrote logic for Inner Packing BOM: Material No. (Now only prompts WARNING if Material No. is completely new)
- Rewrote logic for Inner Packing BOM: Sequence No. (Properly detects duplicate sequence no.)
- Rewrote logic for Parts Master: WEST Fields (Properly accounts for multiple rows in Parts Master)

### Fixed
- Fixed error in get MOD backup row logic that caused program to crash
- Rewrote Supplier Contract: WEST Fields due to it not properly detecting errors

## [1.0.1a] - 2015-12-15
### Fixed
- Fixed error in Customer Parts: Paired Parts that caused program to crash
- Fixed false positives in Customer Parts: Imp Country Code for 'IN, I1, I2, I3' region
- Fixed false positives in Customer Parts: WEST Invoice No. for 'I2' region

## [1.0.1] - 2015-12-15
### Changed
- Both .xls and .XLS files are detected in '1) Submit'

### Removed
- Removed command line output for non-english parts that caused program to crash

### Fixed
- Fixed logic that caused some masters to be incorrectly recognised as not ALL MOD
- Fixed error in Module Group Master check that causes Module Type Master to not be loaded properly
- Fixed error in Parts Master: Exp HS Code that caused program to crash
- Fixed error in Supplier Contract: West Fields that caused program to crash
- Fixed error in Inner Packing BOM: SPQ that caused program to crash
- Fixed error in Customer Parts: Next_SPQ that caused program to crash

## [1.0.0 Stable] - 2015-12-15
### Added
- First build of MCT
