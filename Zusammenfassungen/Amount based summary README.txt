README AMOUNT BASED SUMMARY APPLICATION

This application summarizes a text by extracting the most important sentences. It runs on a simple method using the relative frequency of words in the text.

***Prerequisites:***
Python 3
Python GUI of your choice (My choice: https://www.jetbrains.com/pycharm/)

Python Libraries (with the command to install them via the system command line(cmd)):
pip install nltk
pip install numpy

Before the first start run in python:
import nltk
nltk.download('stopwords')


***Getting started:***
1. Check the prerequisites
2. Start your Python GUI and open the file "summary with only amount.py"
3. Set the necessary variables, provided at the bottom of the application to what fits to your PC.
	"directory" needs to point to the directory at which you have your csv file containing the RSS Feeds
	"number_of_sentences_in_summary" is the number of sentences that the summary will be long. Has to be at least 1 and an integer.
	"summary_file_name" is the name of the file in which the summary will be saved.
4. Run the application.
