from gensim.summarization import keywords
from gensim.summarization.keywords import get_graph
import csv
import os
import json
import re


def import_json(file):
    text = ""
    with open(file) as jsonfile:
        data = json.load(jsonfile)
    for p in data:
        for item in p["text"]:
            text = text + str(item)
        for element in p["texth2"]:
            text = text + str(element)
    return text


def load_text(filename):
    text = ""
    with open(filename, "r") as textfile:
        text = text + textfile.read()
    return text


def load_text_from_directory():
    text = ""
    for file in os.listdir("."):
        if os.path.isfile(file):
            with open(file, "r", encoding="utf8") as textfile:
                text = text + textfile.read()
    return text


def load_text_from_medium_directory():
    text = ""
    for file in os.listdir("."):
        if os.path.isfile(file):
            with open(file, "r", encoding="utf8") as textfile:
                firsttext = textfile.read()
                firsttext = re.sub("TITLE:", " ", firsttext)
                firsttext = re.sub("TEXT:", ".", firsttext)
                text = text + firsttext
    return text


def keyword_extraction(text):
    words = keywords(text, scores=True, lemmatize=True)
    graph = get_graph(text)
    print(graph)
    print(type(graph))
    return words


def export_keywords_to_csv(keywords, file_name):
    csv_file_name = file_name
    with open(csv_file_name, "w", encoding="utf8", newline="") as newWriterFile:
        csvWriter = csv.writer(newWriterFile, delimiter=",")
        for value in keywords:
            csvWriter.writerow(value)
    return csv_file_name


# ------------------------------------------------------------------------------------
# Variables:
export_file_name = "Name.csv"
filename = "TEXT_DATEI.txt" #only if function 'load_text' is used
working_directory = "C:\\DATA\\NLP Testing Clustering\\ergebnisse keyword extraction" #either with // or with \\

# Calls:
# 0. Change dircetory
os.chdir(working_directory)
# 1. Get the text, choose one of the extraction methods
# text = import_json("me.json")
text = load_text(filename)
# text = load_text_from_medium_directory()
# 2. Compute the keywords
keys = keyword_extraction(text)
# 3.Export the keywords
export_keywords_to_csv(keys, export_file_name)
