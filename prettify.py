import json
import openpyxl
from openpyxl import Workbook
import os
import pandas as pd
import sys

def create_file(file_path):
        with open(file_path, "w") as file:
            file.write("Test")

#Parses the JSON object and creates an excel report. 
def generate_excel_report(report_json, input_repository):
    
    excel_file_path = f"{input_repository}/gitleaks_excel.xlsx"
    create_file(excel_file_path)
    
    excel_leaks = Workbook()
    sheet = excel_leaks.active


    headers = ["Description" ,"File Path", "Date", "Author", "Link"]
    row_num = 1
    excel_entries = [[headers]]
    
    

    #data = pd.read_json(report_json)
    for finding in report_json: 
        description = finding["Description"]
        file_path = finding["File"]
        date = finding["Date"]
        author = finding["Author"]
        link = "github.com/" + input_repository + "/" + file_path
        
        values = [description, file_path, date, author, link]

        excel_entries.append(values)

    for row_index, row_data in enumerate(excel_entries, start=row_num):
        for col_index, value in enumerate(row_data, start=1):
            sheet.cell(row=row_index, column=col_index).value = value
    

    
#Grabs the json file and turns it into workable python object for the generate_excel_report method. 
def pass_report(input_repository): 
   
    with open(f"{input_repository}/leaks.json", "r") as f:
        report_json =  json.load(f)
    print(type(report_json))
    generate_excel_report(report_json, input_repository)

#Runs the original gitleaks command to create a json finding with the files.
def run_gitleaks(input_repository):
    try:
        command = f"cd {input_repository} && gitleaks detect -r leaks.json"
        error_check = os.system(command)
        
        if error_check != 0:
            raise Exception("ERROR: Gitleaks did not run successfully \n \n")
    except Exception as e:
        print(str(e))
    


def main(): 
    input_repository = sys.argv[1]
    run_gitleaks(input_repository)
    pass_report(input_repository)


if __name__ == "__main__":
    main() 