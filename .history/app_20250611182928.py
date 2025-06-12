from flask import Flask, render_template, request

import sqlite3


app = Flask(__name__)



connection = sqlite3.connect("users_log.db")



cursor = connection.cursor()


cursor.execute ("""
            CREATE TABLE IF NOT EXISTS users_log (
                
                
                id INTEGER PRIMARY KEU AUTO INCREMENT,


                name TEXT                


                username TEXT
                
                
                email TEXT
                
                
                password TEXT
                
            )   
                """)



@app.route("/", methods=["POST", "GET"])



def home():


    email = request.form.get("email")


    password = request.form.get("passoword")


    return render_template("index.html")


if __name__ == "__main__":


    app.run(debug=True)