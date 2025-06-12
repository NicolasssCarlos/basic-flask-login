from flask import Flask, render_template, request

import sqlite3


app = Flask(__name__)



connection = sqlite3.connect("users_log.db")



cursor = connection.cursor()


cursor.execute ("""
                


            CREATE TABLE IF NOT EXISTS users_log (
                
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,


                name TEXT,                


                username TEXT,
                
                
                email TEXT,
                
                
                password TEXT
                
            )  



                """)



@app.route("/", methods=["POST", "GET"])



def home():


    welcome = error = ""


    if request.method == "POST":


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


def signup():
   

   if request.method == "POST":
      

      errors = []
      

      name = request.form.get("name")


      username = request.form.get("username")


      email = request.form.get("email")


      password = request.form.get("password")


      if name and username and email and password:
         

        cursor.execute("SELECT * FROM users_log WHERE email = ?", (email,))


        if cursor.fetchone():


           errors.append("Email is already in use")


        cursor.execute("SELECT * FROM users_log WHERE username = ?", (username,))


        if cursor.fetchone():


           errors.append("username is already in use")

        if not errors:
         


         cursor.execute("INSERT INTO users_log (name, username, email, password) VALUES (?, ?, ?, ?)", (name, username, email, password))  


         cursor.execute("SELECT * FROM users_log WHERE username = ?", (username))


         user_name = cursor.fetchone()


         welcome = f"Welcome, {user_name}"


        
   return render_template("login.html", errors=errors, welcome=welcome)



if __name__ == "__main__":


    app.run(debug=True)