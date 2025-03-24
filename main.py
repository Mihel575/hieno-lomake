from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')
with open("high_score.txt" , "w") as high_score:
            high_score.write(str(0))

@app.route("/vastaus")
def vastaus():
    uusi_score = random.randint(1,100)
    if uusi_score >= 90:
        uusi_score = random.randint(1,10000000)
    with open("high_score.txt" , "r") as high_score:
        o = high_score.read()
        vanha_score = int(o)
    if uusi_score >= vanha_score:
        with open("high_score.txt" , "w") as high_score:
            high_score.write(str(uusi_score))
        return render_template('ennatys.html', uusi=uusi_score, vanha=vanha_score)
    else:
        return render_template('vastaus.html', uusi=uusi_score, vanha=vanha_score)

if __name__=="__main__":
    app.run()