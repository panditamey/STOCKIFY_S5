import string
import random
import smtplib
import os
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=12))
code = str(res)
file = open('codes/'+code+'read.txt', 'w')
file.write(code)
file.close()

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/yourcode")
def welcome():
    global code
    if os.path.exists('codes/'+code+'.txt'):
        return render_template("yourcode.html", code=code) 
    else:
        res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=12))
        code = str(res)         
        file = open('codes/'+code+'.txt', 'w')
        file.write(code)
        file.close()
        return render_template("yourcode.html", code=code)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8011)
