from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrets, secrets'
import random
x = (random.randint(1,3))

@app.route ('/')
def index():
    return render_template('great_num.html')

@app.route ('/results', methods=['POST'])
def results():
    print (request.form["guess"])
    print (random.randint(1,100))
    i = (int(request.form["guess"]))
    if i > x:
        return render_template ("great_high.html")
    if i < x:
        return render_template ("great_low.html")
    else:
        return render_template("great_correct.html", guess = request.form["guess"])

if __name__=="__main__": 
    app.run(debug=True) 