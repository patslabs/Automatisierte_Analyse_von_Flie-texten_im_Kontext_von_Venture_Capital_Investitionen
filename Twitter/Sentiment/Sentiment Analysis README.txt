README SENTIMENT ANALYSIS APPLICATION

This application carries out a sentiment analysis on a provided text. The text can be a set of tweets obtained by the application "twitter apit.py".


***Prerequisites:***
Python 3
Python GUI of your choice (My choice: https://www.jetbrains.com/pycharm/)

Python Libraries (with the command to install them via the system command line(cmd)):
pip install textblob
pip install textblob-de
pip install nltk
pip install matplotlib

At the first start of the programm run the following command in python:
import nltk
nltk.download('stopwords')


***Getting started:***
1. Check the prerequisites
2. Start your Python GUI and open the file "Sentiment Analysis.py"
3. Set the necessary variables, provided at the bottom of the application.
	"txt_file_directory" and "file_name" are only used if the "load_text()" function is used for loading the text. If that is the case, they refer to the place in which the Text is saved that has to be analyzed. 
	"tweets_filename" is a file in the same siredtory as the application that contains tweets in a .json format. You could get them by using the "twitter api" application.
	"filename_of_csv_file" is the csv file in which the results of the analyzes are saved.
4. If you want to use the application just on some test text, comment all lines in the "Calls:" section using a "#" besides the commands using the functions "load text()" and "semantic_analysis(text)". Un-comment them. 
5. If you want to use the application if a .json file of tweets, do the opposite of point 4. Un-comment the lines described before to be commented and comment the lines described before to be un-commented.
6. If you use it for the twitter application set the further variables for the plotting at the end of the application:
	"plot_name" is the name of the plot. Can be any string, however you want to name it.
	"plot_x_achses" is the name of the x achses of the plot. Make it any string.
	"plot_y_achses" is the same for the y achses of the plot.
	"plot_area" is an integer that descirbes the sizing of the plot. Try out what fits best for your data.
7. Run the file. 
