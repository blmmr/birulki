## Reading MR tech artiles on a kindle

The app scrapes a new article called "Birulki" from [MR.com](https://mobile-review.com/all/articles/birulki/), parses it as a .txt file, and sends to my kindle.

-  Automation of script is done with Crone

- All directories should be changed.

>in article_scraper:
>directory = "/txt_files/"

>in send_email:
>directory = "/txt_files/"

- SMTP port is 465 for mail.ru, it would be different for gmail.com 
