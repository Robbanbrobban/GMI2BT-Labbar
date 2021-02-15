#$env:FLASK_APP = "server2.py"
#flask run
from flask import Flask, request,render_template
import sqlite3

app = Flask(__name__)

#lägger till i min databas
@app.route('/postjson', methods=['POST'])
def add_weather():
    conn = sqlite3.connect('databas.db')
    c = conn.cursor()
    p = (request.json['sensor'], request.json['temperature'], request.json['humidity'], request.json['pressure'], request.json['wind'])
    c.execute('INSERT INTO SensorData (sensor, temperature, humidity, pressure, wind) VALUES(?,?,?,?,?)',p)
    conn.commit()
    return f"Successful"

#läser in ifrån databas till html tablen
@app.route('/')
def w_data():
    conn = sqlite3.connect('databas.db')
    c = conn.cursor()
    c.execute('''SELECT id, date, sensor, temperature, humidity, pressure, wind FROM SensorData''')
    w_data = c.fetchall()
    return render_template ('weather.html', w_data=w_data)
#tar bort min info

@app.route('/delete')
def delete():
    conn = sqlite3.connect('databas.db')
    c = conn.cursor()
    c.execute('''DELETE FROM SensorData''')
    conn.commit()
    return render_template('deleted.html')

app.run(debug=True) 