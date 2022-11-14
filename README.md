# Label Studio Reporter
With these scripts you can merge several *.txt files into one *.txt or *.xlsx format.

* load list of PNG files from *.txt files. 
* for each file: split extension and leave pure file name. 
* write output to new *.txt file or *.xlsx file


## Quick Start
* > git clone git@github.com:golderbom/LS_Report.git
* Create *.txt files with list of frames in input folder
* Open config_ls.json and change "source_path" correspondingly
* Run script depending on the necessary output format (.txt or .xlsx):
 
  > ls_txt_report.py  
  > ls_xlsx_report.py
