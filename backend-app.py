from flask import Flask, render_template, request, send_from_directory, current_app
import os
import json

path = ["home", "arnaud", "Desktop"]
#path = ["run", "media", "arnaud", "TOSHIBA EXT"]

f = open('../database.json')
data = json.load(f)
f.close()

app = Flask(__name__)

@app.route("/")
def home_index():
    return(render_template("index.html"))

@app.route("/browse", methods=["POST", "GET"])
def browse():
    user_c = request.form.get('user', None)
    passwd_c = request.form.get('pass', None)
    print(user_c)
    print(passwd_c)

    for users in data["users"]:
        if user_c == users["user"]:
            if passwd_c == users["passwd"]:
                print("logged, mounting...")

    folder = request.form.get('cliquedfile', None)
    if folder != None:
        if folder == "Back":
            if len(path) > 3:
                path.pop(len(path) - 1)
            else:
                print("error")
        else:
            path.append(folder)
    PATH = ""
    for i in path:
        PATH = PATH + "/" + i
    try:
        os.listdir(PATH + "/")
    except NotADirectoryError:
        if len(path) > 3:
            path.pop(len(path) - 1)
        else:
            print("error")
        PATH = ""
        for i in path:
            PATH = PATH + "/" + i

    dir = os.listdir(PATH + "/")
    dir.append("..")

    return(render_template("browse.html", files = dir))

if __name__ == "__main__":
    app.run(debug=True)
