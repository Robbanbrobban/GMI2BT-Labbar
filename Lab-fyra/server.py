# $env:FLASK_APP = "server.py"
# set FLASK_ENV=development
# run flask
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')#Visar hemsidan med formulär
def subscribe():
    return render_template ('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST": #Hämtar dicten på informationen jag har skrivit i formuläret
        req = request.form
        print(req)
        return render_template ('register.html', result=req)#returnerar resultatet till register html filen
    
app.run(debug = True)
