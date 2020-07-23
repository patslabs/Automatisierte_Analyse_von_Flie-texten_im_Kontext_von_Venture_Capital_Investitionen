import requests
from selenium import webdriver
import time

#Arbeitsablauf
#1. get authorization
def auth_request(client_id, redirect_uri, ):
    token_url = "https://www.linkedin.com/oauth/v2/authorization?" + "response_type=code" + "&client_id=" + client_id + "&redirect_uri=" + redirect_uri
    driver = webdriver.Firefox()
    print(token_url)
    driver.get(token_url)
    while not driver.current_url.startswith("https://patlab.co"):
        time.sleep(1)
    url_code = driver.current_url
    #can be done nicer with a regex
    solo_code = url_code[24:len(url_code)]
    return solo_code

#2. post request
def app_request(code, client_id, client_secret, redirect_uri):
    application_parameters = {"grant_type" : "authorization_code", "code": code,"client_id": client_id, "client_secret": client_secret, "redirect_uri": redirect_uri}
    application_url= "https://www.linkedin.com/oauth/v2/accessToken"
    application_request = requests.post(application_url, data=application_parameters)
    returned_data = application_request.text
    print(returned_data)
    return returned_data

#3. make get requests to the api
def api_get(access_token):
    permission_url = "https://api.linkedin.com/v1/people/~:(first-name)"
    header = {"Authorization": "Bearer " + access_token}
    api_draw = requests.get(permission_url, headers=header)
    api_draw_result = api_draw.text
    print(api_draw_result)
    return


#sign up at the web browser for the access
code = auth_request("86kzeq0vfvmq7l","https://patlab.co")
print("Code is:" + code)
#confirm your permission to LinkedIn
token = app_request(code, "86kzeq0vfvmq7l", "mWGEDeFT4gH7Xnow", "https://patlab.co")[17:-23]
print("Token is:" + token)
#Make the request for data at LinkedIn
api_get(token)


