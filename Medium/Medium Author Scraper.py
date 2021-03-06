import requests
import os
from bs4 import BeautifulSoup
import csv
import re
from statistics import mode


def download_full_side(url, batch_name):
    #get the url, download it, save it as txt file
    text = requests.get(url)
    file_Name = batch_name + "1.html"
    i = 1
    while os.path.isfile(file_Name):
        i += 1
        file_Name = batch_name + str(i) + ".html"

    with open(file_Name, "wb") as HTMLFile:
        for chunk in text.iter_content(100):
            HTMLFile.write(chunk)
    return file_Name


def get_title_and_text(file_name):
    #
    txt_file_name = file_name[:-5] + ".txt"
    with open(file_name, encoding="utf8") as html_file:
        soup = BeautifulSoup(html_file, "html.parser")
        with open(txt_file_name, "w", encoding="utf8") as txt_file:
            txt_file.write("TITLE:" + "\n")
            txt_file.write(str(soup.title.get_text()))
            txt_file.write("\n" + "TEXT:" + "\n")
            for tag in soup.find_all("div"):
                if "section-inner" in tag["class"]:
                    for child in tag.children:
                        if child.name == "p":
                            txt_file.write(child.get_text())
    return


def prettifier_of_file(file_name):
    with open(file_name, encoding="utf8") as textfile:
        soup = BeautifulSoup(textfile, "html.parser")
        print(soup.prettify())
    return


def print_out_hrefs():
    with open("ZweiterTestAuthor1.html", encoding="utf8") as textfile:
        soup = BeautifulSoup(textfile, "html.parser")
        for href in soup.find_all("a"):
            print(href.get("href"))
    return


def get_hrefs_of_author_page(file_name, initial_link):
    href_liste = []
    second_path = False
    regex = re.compile("-{8,9}\d")
    with open(file_name, encoding="utf8") as textfile:
        soup = BeautifulSoup(textfile, "html.parser")
        for href in soup.find_all("a"):
            link = href.get("href")
            if re.search("source=user_profile", link) and re.search("https://", link) and link not in href_liste and link != initial_link:
                href_liste.append(link)
            if href_liste == [] or second_path:
                #This is the second path if they don't write for anyone. Not as safe as I don't see the reason behind it.
                second_path = True
                #Makes sure that after the first link is added to the previously empty list, the other ones can take that path too.
                if re.search(regex, link) and re.search("https://", link) and link not in href_liste:
                    href_liste.append(link)
    return href_liste

def get_hrefs_of_home_page(file_name, initial_link):
    href_liste = []
    second_path = False
    regex = re.compile("-{8,9}\d")
    with open(file_name, encoding="utf8") as textfile:
        soup = BeautifulSoup(textfile, "html.parser")
        for href in soup.find_all("a"):
            link = href.get("href")
            if re.search("source=collection_home", link) and re.search("https://", link) and link not in href_liste and link != initial_link:
                href_liste.append(link)
            if href_liste == [] or second_path:
                #This is the second path if they don't write for anyone. Not as safe as I don't see the reason behind it.
                second_path = True
                #Makes sure that after the first link is added to the previously empty list, the other ones can take that path too.
                if re.search(regex, link) and re.search("https://", link) and link not in href_liste:
                    href_liste.append(link)
    return href_liste


def export_hrefs_to_csv(href_liste, file_name):
    href_csv_file_name = file_name[:-5] + "author_href_list.csv"
    with open(href_csv_file_name, "w", encoding="utf8", newline="") as newWriterFile:
        csvWriter = csv.writer(newWriterFile, delimiter=",")
        for item in href_liste:
            csvWriter.writerow([item])
    return href_csv_file_name


def crawl_secondaries(href_list_file, batchname):
    with open(href_list_file, "r", encoding="utf8") as href_file:
        for href in href_file:
            file_name = download_full_side(href, batchname)
            get_title_and_text(file_name)
    return


def get_author_url(file_name):
    author_links = []
    with open(file_name, encoding="utf8") as html_file:
        soup = BeautifulSoup(html_file, "html.parser")
        for link in soup.find_all("a"):
            link_href = link.get("href")
            if len(link_href) > 20:
                if re.search("medium.com/@", link_href):
                    #Benutzung der re nachdem vorher das hier war: link_href[19] == "@"
                    author_links.append(link_href)
    try:
        #find the most common link in the list which is probably the link for the author
        author_link = mode(author_links)
    except Exception:
        #if there are some links of the same amount existing, it raises a statistics error, so take instead the first one found
        author_link = author_links[0]
    return author_link


#Variablen für die Gesamtapplikation:
#starter_link ="https://medium.com/edtech-trends/this-is-what-the-future-of-mixed-reality-looks-like-34fffeaa07b3"
Batch_name = "deepcode"
Author_Batch_name = Batch_name + "_Author"

#Suche alle links auf der gegebenen Seite, rufe den Standardprozess mit jedem von ihm auf.#
new_starter_link = "https://medium.com/deepcode-ai"
overview_side = download_full_side(new_starter_link, Batch_name)
list_of_first_articles = get_hrefs_of_home_page(overview_side, new_starter_link)
for starter_link in list_of_first_articles:



#Algorithmus für die Aufgabe: Scrape die Seite, Finde den Autor, Lade die ersten 4 Artikel der Autorenseite herunter.
    MAINfile_name = download_full_side(starter_link, Batch_name)

    get_title_and_text(MAINfile_name)

    author_url = get_author_url(MAINfile_name)

    author_file_name = download_full_side(author_url, Author_Batch_name)

    href_liste_of_further_articles = get_hrefs_of_author_page(author_file_name, starter_link)

    href_csv_file_name_from_author_page = export_hrefs_to_csv(href_liste_of_further_articles, MAINfile_name)

    crawl_secondaries(href_csv_file_name_from_author_page, Batch_name)


#Funktionen, die nicht im Hauptprozess genutzt werden:
#print_out_hrefs()
#prettifier_of_file()