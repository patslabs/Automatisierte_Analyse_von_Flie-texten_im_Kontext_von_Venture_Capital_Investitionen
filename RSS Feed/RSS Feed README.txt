README RSS FEED APPLICATION

This application allows the download of content, provided by an RSS Feed, as well as the maintenance of the application itself.

***Prerequisites:***
Python 3
Python GUI of your choice (My choice: https://www.jetbrains.com/pycharm/)

Python Libraries (with the command to install them via the system command line(cmd)):
pip install feedparser
pip install newspaper3k
pip install requests
pip install beautifulsoup4

***Getting started:***
1. Check the prerequisites
2. Start your Python GUI and open the file "RSS Feed.py"
3. If you don't have a csv file with a list of RSS Feed Links in it start using the "csv_rss_adder" to create a csv file containing RSS Adresses.
4. Set the necessary variables, provided at the bottom of the application to what fits to your PC.
	"feed directory" needs to point to the directory at which you have your csv file containing the RSS Feeds
	"feed_filename" is the name of the csv file containing the RSS Feed Links. Add the .csv at the end of the filename.
	"directory_to_save_downloads" is the directory at which you want to save the downloaded text files. Can be anywhere.
5. Run the "execute_the_rss_downloader" command
