import os
import json

from email.mime.text import MIMEText

def list_existing_txt_files(folder_path):
    folder_path = "txt_files"
    text_files = [f for f in os.listdir(folder_path)]
    return text_files

def read_existing_json_files():
    with open('list_of_files.json') as json_file:
        list_of_files = json.load(json_file)
    return list_of_files

def attach_file(folder_path, new_files):
    for file_name in new_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as attachment:
            part = MIMEText(attachment.read(), "plain")
            part.add_header("Content-Disposition", f"attachment; filename={file_name}")
            return part
        
def update_list_of_files(list_of_files, new_files):
    list_of_files.extend(new_files)
    with open('list_of_files.json', 'w') as json_file:
        json.dump(list_of_files, json_file)
