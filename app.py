from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
db = SQLAlchemy(app)
app.app_context().push()


class Employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer, nullable=False)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        salary = request.form.get("salary")
        employee = Employee(name=name, email=email, phone=phone, salary=salary)
        db.session.add(employee)
        db.session.commit()
    allEmployee = Employee.query.all()
    return render_template("home.html", allEmployee=allEmployee)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/Delete/<int:sno>")
def Delete(sno):
    emp = Employee.query.filter_by(sno=sno).first()
    db.session.delete(emp)
    db.session.commit()
    return redirect("/")


@app.route("/Update/<int:sno>", methods=['GET', 'POST'])
def Update(sno):
    emp = Employee.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        emp.name = request.form.get("name")
        emp.email = request.form.get("email")
        emp.phone = request.form.get("phone")
        emp.salary = request.form.get("salary")
        db.session.commit()
        return redirect("/")
    return render_template("update.html", emp=emp)
    

if __name__ == "__main__":
    app.run(debug=True)