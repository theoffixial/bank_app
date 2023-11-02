from flask import Flask, render_template, request
from bank import AccHolder, display_account_info


app = Flask(__name__)




@app.route("/", methods=["GET","POST"])
def deposite():
    if request.method == "GET":
        return render_template("deposite.html")
    elif request.method == "POST":
        acc_number = request.form.get("acc_no")
        acc_name = request.form.get("acc_name")

        acc_holder = display_account_info(acc_number)

        if acc_holder:
            amount = float(request.form.get("amount"))
            balance = acc_holder.deposit(amount)
            return render_template("deposite.html", balance=balance)
            # return render_template("deposite.html", balance=0)

