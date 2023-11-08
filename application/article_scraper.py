import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_text_from_main_section(soup):
    main_section = soup.find('main', class_='section article container')

    p_tags = main_section.find_all('p')  
    article = "\n".join(p.get_text() for p in p_tags)  

    return article

def write_txt_files(number, url):
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    try:
        article=get_text_from_main_section(soup)
    except:
        print("No main section found.")
        exit()

    directory = "/txt_files/"
    file_name = f"{directory}b_{number}.txt"

    current_date = datetime.now().strftime("%d-%m-%Y")

    with open(file_name, "w") as file:
        file.write(current_date + "\n" + article)

    print(f"Wrote file {file_name}")

    