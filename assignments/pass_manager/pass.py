from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("pass_index.html");  
 
@app.route("/add")  
def add():  
    return render_template("add.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "error"  
    if request.method == "POST":  
        try:  
            username = request.form["username"]  
            email = request.form["email"]  
            password = request.form["password"]  
            rank= username[-3:]
            global table
            if rank == 'adm':
                table="admin_cred"
            elif rank == 'sad':
                table="s_admin_cred"
            else:
                table="intern_cred"

            
            with sqlite3.connect("pass_manager.db") as con:  
                cur = con.cursor() 
                exe= "INSERT into {} (username, email, password) values (?,?,?)".format(table)
                cur.execute(exe,(username,email,password))  
                con.commit()  
                msg = "The credentials have been posted on your Facebook wall... JK :P"  
        except:  
            con.rollback()  
            msg = "Ooops! Something went wrong!"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  

@app.route("/view")
def view():
    con=sqlite3.connect("pass_manager.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    exe="select * from {}".format(table)
    cur.execute(exe)
    rows=cur.fetchall()
    return render_template("view.html",rows=rows)

@app.route("/delete")
def delete():  
    return render_template("delete.html")  

@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["userid"]  
    with sqlite3.connect("pass_manager.db") as con:  
        try:  
            cur = con.cursor()  
            exe="delete from {} where userid = ?".format(table)
            cur.execute("delete from credentials where userid = ?",id)  
            msg = "Deleted successfully!"  
        except:  
            msg = "Unable to delete"  
        finally:  
            return render_template("delete_record.html",msg = msg)


if __name__ == "__main__":
    app.run(debug=True)