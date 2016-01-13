import rpweibo
import pyotherside
import json
import urllib.parse
import urllib.request

def login(API_KEY,API_SECRET,REDIRECT_URI,username,password):
    example_app = rpweibo.Application(API_KEY, API_SECRET, REDIRECT_URI)
    weibo = rpweibo.Weibo(example_app)
    authenticator = rpweibo.UserPassAutheticator(username, password)
    try:
        weibo.auth(authenticator)
        access_token,uid = authenticator.auth(example_app)
        print(access_token,uid)
        pyotherside.send("pyhandler",access_token,uid)
    except rpweibo.AuthorizeFailed as e:
        print("Invalid username or password!")
        pyotherside.send("pyhandler","Error",e)
    except rpweibo.APIError as e:
        print("Api Error")
        pyotherside.send("pyhandler","Error",e)
