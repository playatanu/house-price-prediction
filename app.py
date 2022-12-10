from flask import Flask, request
from flask_mysqldb import MySQL
from pricePredic import predict

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6583315'
app.config['MYSQL_PASSWORD'] = 'Yp19mUMsJF'
app.config['MYSQL_DB'] = 'sql6583315'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


def getHouseList():
    cur = mysql.connection.cursor()
    cur.execute("select sqrt,bedrooms,bathrooms,price,latitude,longitude from houses")
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return rv

@app.route('/')
def home():
    return {"About":"house price predicition api","Author":"Atanu Debnath"}

@app.route('/predic')
def predic():

    data =  {"sqrt" : int(request.args.get('sqrt')),
            "bed" : int(request.args.get('bed')),
            "bath":int(request.args.get('bath')),
            "lat":float(request.args.get('lat')),
            "lng":float(request.args.get('lng'))
             }

    return {"estimate" : predict(data['sqrt'],data['bed'],data['bath'],data['lat'],data['lng'],getHouseList())}

app.run(debug=True)