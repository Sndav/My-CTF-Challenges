var express = require('express');
var app = express();
var session = require('express-session');
var cookieParser = require('cookie-parser');
const bodyParser = require('body-parser')
var fs = require("fs")

session_secret = Math.random().toString(36).substr(2);
app.use(bodyParser.json())
app.use(cookieParser(session_secret));
app.use(session({
    secret: session_secret,
    resave: true,
    saveUninitialized:true
}));

function copyArray(arr1){
    var arr2 = new Array(arr1.length);
    for (var i=0;i<arr1.length;i++){
        if(arr1[i] instanceof Object){
            arr2[i] = copyArray(arr1[i])
        }else{
            arr2[i] = arr1[i]
        }
    }
    return arr2
}

app.get('/', function (req, res) {
  res.send('Confuse you! SEE `/src`');
});

app.post('/login',function(req,res){
    var usernames = req.body.usernames
    // check username array
    for(var i=0;i<usernames.length;i++){
        if(usernames[i] == 'admin'){
            res.send('go hacker!')
            return
        }
    }
    req.session.users = copyArray(usernames)
    res.send('Success')
})

app.get('/getflag',function(req,res){
    if(req.session.users ){
        for(var i=0;i<req.session.users.length;i++)
            if(req.session.users[i] == 'admin'){
                var data = fs.readFileSync('/flag')
                res.send(data.toString())
                return
            }
    }else{
        res.send("Please be admin")
        return
    }
})

app.get('/src', function (req, res) {
    var data = fs.readFileSync('app.js');
    res.send(data.toString());
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
