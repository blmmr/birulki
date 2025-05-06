# 📖 Read MR Tech Articles on Kindle
This Python script automates the process of sending new *Birulki* articles from [Mobile-Review.com](https://mobile-review.com/all/articles/birulki/) to your Kindle as `.txt` files.

## ✨ Features
- Scrapes the latest *Birulki* article.
- Converts the article to plain text.
- Emails the file to your Kindle.
- Can be automated with a **cron job**.

## 🔧 Configuration
Update the target directories in the following files:
~~~python
# article_scraper.py
directory = "/txt_files/"

# send_email.py
directory = "/txt_files/"
~~~

## 📤 Email Settings
- Uses SMTP to send the email.
- Default config is for mail.ru using port 465.
- For other providers (e.g., Gmail), update the SMTP settings accordingly.

## 🕒 Automation
Set up a cron job to run the script at your preferred interval for full automation.
