from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')
with open("high_score.txt" , "w") as high_score:
            high_score.write(str(0))
with open("high_name.txt" , "w") as high_name:
            high_name.write('eetu')

@app.route("/vastaus")
def vastaus():

    with open("high_score.txt" , "r") as high_score:
        o = high_score.read()
        vanha_score = int(o)
    with open("high_name.txt" , "r") as high_name:
        vanha_nimi = high_name.read()

    uusi_nimi = request.args['uusi_nimi']

    uusi_score = random.randint(1,100)
    if uusi_score >= 50:
        uusi_score = random.randint(1,10000000)
    if uusi_score >= 7500000:
        uusi_score = random.randint(1,1000000000000)

    if uusi_score >= vanha_score:
        with open("high_score.txt" , "w") as high_score:
            high_score.write(str(uusi_score))
        if uusi_nimi == "":
            uusi_nimi = "Anonyymi ukkeli"
        with open("high_name.txt" , "w") as high_name:
            high_name.write(uusi_nimi)
        return render_template('ennatys.html', uusi_score=uusi_score, vanha_score=vanha_score, uusi_nimi=uusi_nimi, vanha_nimi=vanha_nimi)
    else:
        return render_template('vastaus.html', uusi_score=uusi_score, vanha_score=vanha_score, vanha_nimi=vanha_nimi)

if __name__=="__main__":
    app.run()