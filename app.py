from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:haianh@localhost:5432/haianh"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class EmployeesModel(db.Model):
    __tablename__ = 'employees'

    employeeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<Employee {self.name}>"


@app.route('/')
def hello():
	return {"hello": "world"}


@app.route('/employees', methods=['POST', 'GET'])
def handle_employees():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_employee = EmployeesModel(name=data['name'], username=data['username'], password=data['password'])
            db.session.add(new_employee)
            db.session.commit()
            return {"message": f"employee {new_employee.username} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        employees = EmployeesModel.query.all()
        results = [
            {
                "name": employee.name,
                "username": employee.username,
                "password": employee.password
            } for employee in employees]

        return {"count": len(results), "employees": results, "message": "success"}


@app.route('/employees/<employee_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_employee(employee_id):
    employee = EmployeesModel.query.get_or_404(employee_id)

    if request.method == 'GET':
        response = {
            "name": employee.name,
            "username": employee.username,
            "password": employee.password
        }
        return {"message": "success", "employee": response}

    elif request.method == 'PUT':
        data = request.get_json()
        employee.name = data['name']
        employee.username = data['username']
        employee.password = data['password']

        db.session.add(employee)
        db.session.commit()
        
        return {"message": f"employee {employee.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(employee)
        db.session.commit()
        
        return {"message": f"Employee {employee.name} successfully deleted."}


if __name__ == '__main__':
    app.run(debug=True)