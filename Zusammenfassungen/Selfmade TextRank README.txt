README SELFMADE TEXTRANK APPLICATION

This application summarizes a textfile by extracting the most important sentences. It uses the TextRank Algorithm.

***Prerequisites:***
Python 3
Python GUI of your choice (My choice: https://www.jetbrains.com/pycharm/)

Python Libraries (with the command to install them via the system command line(cmd)):
pip install numpy
pip install pandas
pip install nltk
pip install sklearn
pip install networkx

Go to: https://nlp.stanford.edu/projects/glove/
Download the glove.6b.zip file
Unzip it in any directory.
Remember the path for the variables.

Before running the application the first time run the following python script:
import nltk
nltk.download('stopwords')
nltk.download('punkt')


***Getting started:***
1. Check the prerequisites
2. Start your Python GUI and open the file "Build your own TextRank.py"
3. Set the necessary variables, provided at the bottom of the application to what fits to your PC.
	"filename" needs to point to the directory at which you have your csv file containing the RSS Feeds
	"directory" is the path at which the file with the name of "filename" can be found.
	"path_for_vector_file" is the file that you downloaded before and saved anywhere. Take the absolut path of that file.
	"summary_length_in_sentences" is the number of sentences a summary can be long. Has to be an integer and 1 or more.
	"summary_filename" is the name of the file that will contain the summary. Add a .txt at the end and let it be a new file.
4. Run the application 
5. Optional: You can export the values of the single sentences by un-commenting the "export_raw_sentence_values_to_csv" function.
