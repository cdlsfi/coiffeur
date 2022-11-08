from http.client import OK
from flask import Flask, render_template, request
import sqlite3 as sql
app=Flask(__name__)
                                                                        
@app.route("/")
def home():
    return render_template("index.html")
    return render_template(".html")
@app.route("/reservation", methods=["POST"])
def reservation():
    nom = request.form['nom']
    prenom = request.form['prenom']
    date = request.form['date']
    heure = request.form['heure']
    telephone = request.form['telephone']
    suggestion = request.form['suggestion']
    connection = sql.connect("db.db")




    cursor = connection.cursor()
    query = f'insert into reservation (nom, prenom, date, heure, telephone, suggestion) values ("{nom}", "{prenom}", "{date}", "{heure}", "{telephone}", "{suggestion}")'
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
    except sql.Error as e:
        print(e)

        connection.rollback()
    connection.close()


    return render_template("merciavotrevisite.html")

if __name__=="__main__":
    app.run()