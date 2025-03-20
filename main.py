from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    #uusi_nimi = request.args['nimi']
    uusi_nimi = random.randint(1,100)
    if uusi_nimi >= 70:
        uusi_nimi = random.randint(1,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    #with open("kaikki_nimet.txt" , "a") as nimitiedosto:
        #nimitiedosto.write(uusi_nimi + "   VALI   "+ "\n")
        #kaikki_nimet = open('kaikki_nimet.txt').read()
    return render_template('vastaus.html', nimi=uusi_nimi)
    #return render_template('vastaus.html', nimi=request.args['nimi'])

if __name__=="__main__":
    app.run()