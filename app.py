 # step one banking app
from flask import Flask, render_template, request, session, url_for, redirect
from function import Bank

app = Flask(__name__)
users = {}
print(users)
app.secret_key = 'qwertyuiop1234[]qwddqwwEsdcsd'


@app.route('/')
def homepage():
    return render_template('homepage.html') 

@app.route('/register', methods = ['GET','POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']

       
        if username in users:
            print('User alredy exist')
            return render_template('register.html')
        else:
            password = request.form['password']
            users[username] = password
            print('succsesful')
            print(users)
            return render_template('homepage.html')
    else:
        return render_template('register.html')
@app.route('/deposite', methods=['GET', 'POST'])
def deposite():
    if request.method == 'POST':
        amount = request.form['deposite']
        user.deposite(amount)
        print(user.show_details())  # Call the show_details() method
        return render_template('deposite.html')
    else:
        return render_template ('deposite.html')






@app.route('/withdrawal', methods=['GET', 'POST'])
def withdrawal():
    if request.method == 'POST':
        amount = request.form.get('withdrawal')
        if amount is not None:
            user.withdrawal(amount)
            print(user.show_details())  # Call the show_details() method
        return render_template('withdrawal.html')
    else:
        return render_template('withdrawal.html')


@app.route('/login',methods = ['GET','POST'])
def login():
    global user
    if request.method =='POST':
        username =request.form['username']
        password =request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            user = Bank(session['user'])
            print(user.show_details())
            print('Login succsesfull')
            return render_template('deposite.html')
    else:
        print('Username dosent exist or incorrect password')
        return render_template('login.html')

    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= '8000',
    debug=True)