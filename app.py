
""" from crypt import methods """
from email import message
from http import client

import collections
from lib2to3.pgen2 import driver
from unittest import result
import pymongo

client=pymongo.MongoClient("mongodb+srv://user:user123@new.ky4ln.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.member_system


from flask import*



app=Flask (
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="any string but secret"
@app.route("traning/")
def index():
    return render_template("index.html")

@app.route("traning/member")
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("traning/")

@app.route("traning/error")
def error():
    message=request.args.get("msg","發生錯誤,請聯繫客服")
    return render_template("error.html",message=message)

@app.route("traning/signup",methods=["post"])
def signup():
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    collection=db.user
    result=collection.find_one({
        "email":email
    })
    if result != None:
        return redirect("traning/error?msg=信箱已被註冊")
    collection.insert_one({"nickname":nickname,"email":email,"password":password
    })
    return redirect("traning/")


@app.route("traning/signin",methods=["post"])
def signin():
    email=request.form["email"]
    password=request.form["password"]
    collection=db.user

    result=collection.find_one({
         "$and":[
            {"email":email},
            {"password":password}
         ]
     })
    if result==None:
        return redirect("traning/error?msg=帳號或密碼錯誤")
    session["nickname"]=result["nickname"]
    return redirect("traning/member")

@app.route("traning/signout")
def signout():
    del session["nickname"]
    return redirect("traning/")




app.run(debug=True")
