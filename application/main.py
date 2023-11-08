import smtplib
from email.mime.multipart import MIMEMultipart

from article_scraper import *
from send_email import *

'''Writing articles as txt files'''

number = 770

while True:
    url = f"https://mobile-review.com/all/articles/birulki/biryulki-n{number}"
    response = requests.get(url)

    if response.status_code == 200:
        write_txt_files(number, url)
        number += 1
    else:
        print("Response status code is not 200.")
        break


'''Sending emails with txt files as attachments'''

msg = MIMEMultipart()
msg["From"] = "who_is_sending_the_email@mail.ru"
msg["To"] = "your_address@kindle.com"
msg["Subject"] = "Birulki"

email_from = "who_is_sending_the_email@mail.ru"
email_to = "your_address@kindle.com"

folder_path = "/txt_files/" #  path to the txt_files

text_files = list_existing_txt_files(folder_path)
list_of_files = read_existing_json_files()

new_files = [f for f in text_files if f not in list_of_files]

if new_files:
    print("New .txt files found:")
    for new_file in new_files:
        print(new_file)
else:
    print("No new .txt files found.")
    quit()

part = attach_file(folder_path, new_files)
msg.attach(part)

'''Connecting to server and sending an email'''
server = smtplib.SMTP_SSL('smtp.mail.ru', 465) 
server.login("who_is_sending_the_email@mail.ru", "password")

server.sendmail(email_from, email_to, msg.as_string())
server.quit()

update_list_of_files(list_of_files, new_files)