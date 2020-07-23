README CLUSTERING WITH EXTERNAL LIB APPLICATION

This application can cluster text documents depending on their content and predict for a new document to which cluster it would fit.

***Prerequisites:***
Python 3
Python GUI of your choice (My choice: https://www.jetbrains.com/pycharm/)

Python Libraries (with the command to install them via the system command line(cmd)):
pip install sklearn


***Getting started:***
1. Check the prerequisites
2. Start your Python GUI and open the file "RSS Feed.py"
3. If you don't have a csv file with a list of RSS Feed Links in it start using the "csv_rss_adder" to create a csv file containing RSS Adresses.
4. Set the necessary variables, provided at the bottom of the application to what fits to your PC.
	"directory" is the folder in which a batch of .txt files is saved. Those files are the files to build closters with. Do not have anything else in those directories.
	"amount_of_clusters" is the amount of different clusters you want to have at the end.
	"prediction_text" is optional. If you want to try out how the prediction works you can save there a text that after building the clusters the algorithm will assign to one of the clusters.
5. Run the application
6. Optional is to do a prediction on the text saved in "prediction_text". Can be done by un-commenting the "prediction()" call.
