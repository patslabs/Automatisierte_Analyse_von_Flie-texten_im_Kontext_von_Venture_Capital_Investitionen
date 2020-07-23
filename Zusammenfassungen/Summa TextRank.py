from summa.summarizer import summarize
import os


def summarize_text(file_name):
    with open(file_name, "r", encoding="utf8") as text:
        texte = text.read()
        summ = summarize(texte, ratio=0.1, language="english")
    return summ


def export_summary_to_txtfile(summary, filename):
    with open(filename, "w", encoding="utf8") as file:
        for line in summary:
            file.write(line)
    return

# ------------------
# Variables:
directory = "C:\\DATA\\NLP Testing\\medium test data, deepcodeAI\\deepcode test"
file_name = "FILE_NAME.txt"
summary_file_name = file_name[:-4] + "_summary.txt"

# Calls:
os.chdir(directory)
# 1. summarize the text using the library summa
summary = summarize_text(file_name)

# 2. Export the summary to a txt file
export_summary_to_txtfile(summary, summary_file_name)
