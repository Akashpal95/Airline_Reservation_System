from flask import Flask,render_template,url_for,redirect,request,json,flash,jsonify,session
from datetime import datetime
import time
import pymysql
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def main():
    return render_template("LoginPage.html")


@app.route('/signin',methods=['POST'])
def signin():
    session['user_name']=request.form['user_name']
    return render_template('SearchPage.html',user_name=session['user_name'])

@app.route('/bookingStatus/<somevar>')
def bookingStatus(somevar):
    print(somevar)
    return render_template('ConfirmPage.html',bk_id=somevar)


@app.route('/book',methods=['GET','POST'])
def book():
    Flight_id=request.form['Flight_id']
    First_name=request.form['First Name']
    Last_name=request.form['Last Name']
    phn_no=request.form['phone_no']
    email_id=request.form['Email_id']
    db=pymysql.connect("localhost","root","","Airlines" )
    cursor = db.cursor()
    print("i am here")
    #cursor.callproc('sp_book',(Flight_id,First_name,Last_name,phn_no,email_id))
    #cursor.execute('INSERT INTO `Bookings` (Flight_name,First_name,Last_name,Phone_no,Email_id) VALUES ("%s")(Flight_id,First_name,Last_name,phn_no,email_id)')
    insertstr="INSERT INTO `Bookings` (Flight_name,First_name,Last_name,Phone_no,Email_id) VALUES "+"(\""+Flight_id+"\",\""+First_name+"\",\""+Last_name+"\",\""+phn_no+"\",\""+email_id+"\")"
    cursor.execute(insertstr)
    db.commit()
    cursor.execute("SELECT booking_id from `bookings` ORDER BY booking_id DESC")
    booking_id=cursor.fetchone()
    print(booking_id)
    empdict={
    'booking_id':booking_id
    }
    return jsonify(empdict)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    db=pymysql.connect("localhost","root","","Airlines" )
    cursor = db.cursor()
    Departure=request.form['Departure']
    Arrival=request.form['Arrival']
    Passengers=request.form['Passengers']
    sql="SELECt r.Flight_name,r.Departure_time,r.Arrival_time,r.Price FROM `flights` as r WHERE r.Departure='%s' and r.Arrival='%s'" %(Departure,Arrival)
    '''if(seat !='0'):
        sql="SELECt r.block,r.floor,r.wing,r.seater,r.room_id FROM `rooms` as r WHERE r.seater='%s' and r.block='%s'" %(seat,block)
    else:
        sql="SELECt r.block,r.floor,r.wing,r.seater , r.room_id  FROM `rooms` as r WHERE r.block='%s'" %(block)    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    somedict={}
    somedict.clear()
    somedict={
        "Flight_name": [ x[0] for x in result ],
        "Departure_time": [ x[1] for x in result ],
        "Arrival_time":[ x[2] for x in result ],
        "Price":[x[3] for x in result ]
    }
    return jsonify(somedict)

if __name__ == "__main__":
    app.secret_key = 'csjgadsjasglGYVG'
    app.run()