import feedparser
import csv
import os
from newspaper import Article
import newspaper
import re
import requests
from bs4 import BeautifulSoup
import urllib.request


def csv_rss_adder(filepath, filename):
#add a new rss feed to your existing rss library
    yes_matrix = ["y", "yes", "j", "Ja"]

    if filepath:
        print("Your current filepath is:" + filepath + " Do you want to change it?(Y/N)")
        if input() in yes_matrix:
            print("Give me the file path:")
            filepath = input()
    if filename:
        print("Your current filename is:" + filename + " Do you want to change it?(Y/N)")
        if input() in yes_matrix:
            print("Give me the name of the file.")
            filename = input()
    print("Give me the added rss feed")
    rss_feed = input()
    os.chdir(filepath)
    csvfile = open(filename, "a", newline="")
    csv_file_writer = csv.writer(csvfile, delimiter = ",")
    csv_file_writer.writerow([rss_feed])
    csvfile.close()
    print("Thx, I did append the new feed called:" + rss_feed)
    return


def RSS_url_finder(website_url):
#searches for an rss feed on the given website.
    page = urllib.request.urlopen(website_url)
    soup = BeautifulSoup(page, "html.parser")

    link = soup.find_all('link', type='application/rss+xml')
    if link:
        for single_link in link:
            print(single_link.get("href"))
    else:
        print("An error occured, no link was found")
    return()

#Functions for main code:

def read_csv_to_list(filepath, filename):
#this loads a csv file into a list
    output_list = []
    os.chdir(filepath)
    csvfile = open(filename)
    CSV_reader = csv.reader(csvfile)
    output_list = list(CSV_reader)
    return(output_list)

def rss_feedparser_get_link_of_post(rss_url, feednumber):
#gets link of given feednumber
    doc = feedparser.parse(rss_url)
    link = doc.entries[feednumber].link
    return(link)

def create_file_name(website_url, date):
#create a filename for saving the raw text data
    GERcharacters = ["Ü", "ü", "Ä", "ä", "Ö", "ö"]
    INTcharacters = ["Ue", "ue", "Ae", "ae", "Oe", "oe"]
    url = website_url
    article = Article(url)
    article.download()
    article.parse()
    title = article.title
    newsi = newspaper.build(website_url)
    brandtitle = newsi.brand
    name = date + ";_" + title + ";_" + brandtitle
    for i in range(len(GERcharacters)):
        name = name.replace(GERcharacters[i], INTcharacters[i])
    newName = re.sub(r"[^a-zA-Z0-9,.;]", " ", name)
    return(newName)


def rss_feedparser_get_publish_date(rss_url, feednumber):
#gets the publishing date of the post
    doc = feedparser.parse(rss_url)
    publishing_date = doc.entries[feednumber].published_parsed
    Date = str(publishing_date.tm_mday) + "." + str(publishing_date.tm_mon) + "." + str(publishing_date.tm_year)
    return(Date)

def get_raw_text_from_website_directly(website_url):
    url = website_url
    article = Article(url)
    article.download()
    article.parse()
    return(article.text)

def save_text_as_txt(website_url, directory, pub_date):
    os.chdir(directory)
    filename = create_file_name(website_url, pub_date) + ".txt"
    if os.path.isfile(filename):
        return
    else:
        file = open(filename, "w")
        textData = get_raw_text_from_website_directly(website_url)
        file.write(textData)
        file.close()
    return


def start_the_magic(directory_of_csv, csv_name, directory_to_save_txtFiles, number_of_posts):
    rss_feed_list = read_csv_to_list(directory_of_csv, csv_name)
    for element in rss_feed_list:
        try:
            for i in range(0, number_of_posts):
                link = rss_feedparser_get_link_of_post(element[0], i)
                try:
                    publish_date = rss_feedparser_get_publish_date(element[0], i)
                except Exception:
                    publish_date = "unknown_date"
                save_text_as_txt(link, directory_to_save_txtFiles, publish_date)
        except Exception:
            print("The following RSS URL returned an error: " + str(element[0]))
            pass
        print("The download was successfull for element:" + str(element[0]))
    print("Process finished.")
    return()


# Optional:
# Those functions are not included in the main programm here.

def rss_feedparser_get_last_post_title(rss_url):
#gets last post of given rss feed
    doc = feedparser.parse(rss_url)
    title = doc.entries[0].title
    entitie = doc.feed.title
    return("Feed: " + entitie + " ,Titel: " + title)

def rss_feedparser_get_last_post_content(rss_url):
#gets last post of given rss feed
    doc = feedparser.parse(rss_url)
    title = doc.entries[0].title
    description = doc.entries[0].description
    link = doc.entries[0].link
    entitie = doc.feed.title
    return_text = "Feed: " + entitie + " ,Titel: " + title + " ,Beschreibung: " + description + " ,Link: " + link
    return(return_text)

def website_als_txt(website, Ablageort, Doc_name):
    #get's a website and saves the HTML code as a .txt file
    os.chdir(Ablageort)
    doc = requests.get(website)
    if doc.status_code == 200:
        print("The file was successfully downloaded.")
    elif doc.status_code == 404:
        print("The file couldn't be found. Error #404")
    else:
        print("An error occured while downloading the file.")

    #write the website into a file
    File_name = Doc_name + ".html"
    if os.path.isfile(File_name):
        print("The file already exists.")
        #Hier noch daran arbeiten was passiert wenn es das File schon gibt.
    file = open(File_name, "wb")
    for chunck in doc.iter_content(1000):
        file.write(chunck)
    file.close()
    print("The File with the name:" + File_name + " was saved.")
    return()

# ----------------------------------------------------
# Variables:
# for the function 'csv_rss_adder':
filepath = "C:\DATA\Python coding"
filename = "NAME.csv"

# for the function 'start_the_magic':
directory_of_csv = "C:\DATA\Tatsächliche Projekte für die Bachelorarbeit, Datenbeschaffung\RSS Feed"
csv_name = "Apfel.csv"
directory_to_save_txtFiles = "C:\DATA\Tatsächliche Projekte für die Bachelorarbeit, Datenbeschaffung\RSS Feed\Gesammelte Werke"
number_of_posts = 10

# Commands:
# csv_rss_adder()
start_the_magic(directory_of_csv, csv_name, directory_to_save_txtFiles, number_of_posts)

# optional:
# RSS_url_finder("https://www.bvkap.de/")

