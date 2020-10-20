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
