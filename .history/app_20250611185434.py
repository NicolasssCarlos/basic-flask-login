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


    password = request.form.get("password")


    cursor.execute("SELECT * FROM users_log WHERE email = ?", (email, ))


    user_found = cursor.fetchone()


    if user_found:


       password_right = user_found[4]


       if password_right == password:
           
          welcome = f"Welcome, {user_found[1]}"


       else:


           error = "Login failed. Incorrect email or password"



    return render_template("index.html", welcome=welcome, error=error)


if __name__ == "__main__":


    app.run(debug=True)