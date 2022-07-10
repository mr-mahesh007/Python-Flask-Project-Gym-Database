from flask import *
import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mahesh"
    )

cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")
   
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact1.html")


@app.route("/allusers")
def allusers():
    cursor.execute("select * from client")
    data = cursor.fetchall()
    return render_template("allusers.html",userdata = data)

@app.route("/create",methods=["POST"])
def create():
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    username1 = request.form.get('username1')
    insq = "insert into client(Name,Gender,Contact,Email,Password) values ('{}','{}','{}','{}','{}')".format(name,gender,phone,email,username1)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("index"))
    except:
        db.rollback()
        return "Error query"
    
@app.route("/delete")
def delete():
    id = request.args.get('id')
    delq = "delete from client where id={}".format(id)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in query"
    
    
@app.route("/edit")
def edit():
    id = request.args.get('id')
    selq = "select * from client where id={}".format(id)
    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("update.html",row=data)


@app.route("/edit",methods=["POST"])
def update():
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    jdate = request.form.get('jdate')
    feespaid = request.form.get('feespaid')
    pendingfees = request.form.get('pendingfees')
    trainer = request.form.get('trainer')
    weight = request.form.get('weight')
    username1 = request.form.get('username1')
    email = request.form.get('email')
    uid = request.form.get('uid')
    updq = "update client set Name='{}',Gender='{}',Contact='{}',Joining_Date='{}',Fees_Paid='{}',Pending_Fees='{}',Trainer_Name='{}',Weight='{}',Password='{}',Email='{}' where id='{}'".format(name,gender,phone,jdate,feespaid,pendingfees,trainer,weight,username1,email,uid)
    try:
        cursor.execute(updq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error query"
        
'''msg = "Some went wrong"
if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    username = request.form['username']
    password = request.form['password']
    cursor.execute('select * from client where username = %s AND password = %s',(username,password))
    account = cursor.execute.fetchone()
    if account:
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        return redirect(url_for('homepage'))
    else:
        msg = 'Incorrect Username or Password!'

return render_template('index.html', msg==msg)

# ERROR IN UPDATE >> Done
# NO ANY ERROR >>
# Can't validate username and password for login >>'''



if __name__=='__main__':
    app.run()
    
    