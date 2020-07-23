README LINKEDIN API CONNECTION APPLICATION

This application connects with the LinkedIn Api and makes a call for the first name of the signed in person.

***Prerequisites:***
Python 3
Mozilla Firefox webbrowser (the newest version of it, it does not work with another webbrowser)
Python GUI of your choice (My choice: https://www.jetbrains.com/pycharm/)
LinkedIn Developer Account (https://www.linkedin.com/developers/)
A normal LinkedIn Account for testing puposes

Python Libraries (with the command to install them via the system command line(cmd)):
pip install selenium

Install Geckodriver, follow the following links to do that:
Explanation: https://stackoverflow.com/questions/41190989/how-do-i-install-geckodriver
Download: https://github.com/mozilla/geckodriver/releases


***Getting started:***
1. Check the prerequisites
2. Create a new APP at your LinkedIn Developer account and safe the provided keys. Alternatively use the keys of an existing LinkedIn app that you own.
3. Start your Python GUI and open the file "LinkedIn API connection.py"
4. Set the necessary variables, provided at the bottom of the application.
	"client_id" is the client id of your LinkedIn application. 
	"client_secret" is the client secret of your LinkedIn application.
	"redirect_uri" is the uri that a user gets redirected to after he signed in to your application. Theoretically it can be any uri but if it is not yours, the third party may receive the information of your communication with the person that logged in.
			So better use your own. Localhost does not work. For testing purposes, use the one provided in the app, its save. ;)
5. Run the file
