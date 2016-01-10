import rpweibo
import pyotherside
import urllib.request
import json
import urllib.parse
import urllib.request

def login(API_KEY,API_SECRET,REDIRECT_URI,username,password):
    example_app = rpweibo.Application(API_KEY, API_SECRET, REDIRECT_URI)
    weibo = rpweibo.Weibo(example_app)
    authenticator = rpweibo.UserPassAutheticator(username, password)
    try:
        weibo.auth(authenticator)
        access_token = authenticator.auth(example_app)
        uid = getUid(access_token)
        print(access_token,uid)
        pyotherside.send("pyhandler",access_token,uid)
    except rpweibo.AuthorizeFailed:
        print("Invalid username or password!")
        pyotherside.send("pyhandler","Error","Invalid username or password!")


def getUid(access_token):
    url = "https://api.weibo.com/oauth2/get_token_info"
    data = urllib.parse.urlencode({
                    "access_token":access_token
                })
    data = data.encode('utf-8')
    request = urllib.request.Request(url)
    f = urllib.request.urlopen(request, data)
    f = f.read()
    jsondata = json.loads(f.decode("UTF-8"))
    return jsondata["uid"]
