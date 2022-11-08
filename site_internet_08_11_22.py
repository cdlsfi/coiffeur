from http.client import OK
from flask import Flask, render_template, request
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    return render_template("info.html")
@app.route("/reservation", methods=["POST"])
def reservation():
    couleur=request.form['Qelle couleur désirez vous?']
   
    question = request.form['Ecrivez votre question ici']
    connection = sql.connect("db.db")




    cursor = connection.cursor()
    query= f'insert into reservation (couleur, question) valures ("{couleur}", "{question}")'
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
    except sql.Error as e:
        print (e)

        connection.rollback()
    connection.close()

    return render_template("pagedaccueil08_11_22.html")
if __name__=="__main__":
    app.run()

