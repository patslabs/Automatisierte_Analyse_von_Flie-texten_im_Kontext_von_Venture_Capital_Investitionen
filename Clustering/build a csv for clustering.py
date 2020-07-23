import re
import os

def export_to_csv(text_list, file_name):
    href_csv_file_name = file_name
    with open(href_csv_file_name, "w", encoding="utf8") as csv_file:
        csv_file.write("raw.title" + "\n")
        for i in range(len(text_list)):
            value = text_list[i]
            csv_file.write(value + "\n")
    return href_csv_file_name


def load_files_to_list(filename):
    with open(filename, "r") as file:
        text = file.read()
        text = re.sub("\s+", ' ', text)
        text = re.sub(",", " ", text)
        text = re.sub("TITLE:", " ", text)
        text = re.sub("TEXT:", " ", text)
    return text


# --------------------------------------
# Variables:
directory = "C:\\DATA\\NLP Testing Clustering\\clustering test data"
file_name_to_save = "Name.csv"
text = []

# Calls:
os.chdir(directory)
for file in os.listdir("."):
    if os.path.isfile(file):
        file_text = load_files_to_list(file)
        print("text" + file_text)
        text.append(str(file_text))

print(text)
export_to_csv(text, file_name_to_save)
