import os
import pandas as pd
import json


#Parses the JSON object and creates an excel report. 
def generate_excel_report(report_json, input_repository):
    #TODO Write column headers 
    data = pd.read_json(report_json)
    for finding in data: 
        description = data["description"]
        file_path = data["file"]
        date = data["date"]
        author = data["author"]
        link = "placeholder.com" + input_repository + file_path
        #TODO create entry in excel here

    
#Grabs the json file and turns it into workable python object for the generate_excel_report method. 
def pass_report(input_repository): 
    print("test")
    with open(f"/report/{input_repository}", "r") as f:
        report_json =  json.load(f)

    generate_excel_report(report_json, input_repository)

#Runs the original gitleaks command to create a json finding with the files.
def run_gitleaks(input_repository):
    command = f"gitleaks -detect -o /report/{input_repository} {input_repository}"
    os.system(command) 


def main(): 
    input_repository = "test"
    run_gitleaks(input_repository)
    pass_report(input_repository)


if __name__ == "__main__":
    main() 