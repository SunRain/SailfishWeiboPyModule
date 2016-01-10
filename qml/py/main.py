import rpweibo
import pyotherside

def login(API_KEY,API_SECRET,REDIRECT_URI,username,password):
    example_app = rpweibo.Application(API_KEY, API_SECRET, REDIRECT_URI)
    weibo = rpweibo.Weibo(example_app)
    authenticator = rpweibo.UserPassAutheticator(username, password)
    try:
        weibo.auth(authenticator)
        access_token = authenticator.auth(example_app)
        uid = weibo.post("oauth2/get_token_info")["uid"]
        print(access_token,uid)
        pyotherside.send("pyhandler",access_token,uid)
    except rpweibo.AuthorizeFailed:
        print("Invalid username or password!")
        pyotherside.send("pyhandler","Error","Invalid username or password!")
