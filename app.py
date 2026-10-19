from flask import Flask, render_template, request, redirect, url_for,flash
import pyodbc
from db import get_connection

app=Flask(__name__)
app.secret_key="change-this-to-any-random-text"

COLUMNS = "EmployeeID, FullName, Email, Department, Status"
@app.route("/")
def index():
    search = request.args.get("search", "").strip()
    conn = get_connection()
    cursor = conn.cursor()
    if search:
        cursor.execute(
            f"SELECT {COLUMNS} FROM Employees "
            "WHERE FullName LIKE ? OR Department LIKE ? ORDER BY EmployeeId",
            f"%{search}%", f"%{search}%",
        )
    else:
        cursor.execute(f"SELECT {COLUMNS} FROM Employees ORDER BY EmployeeId")
    employees = cursor.fetchall()
    conn.close()
    return render_template("index.html", employees=employees, search=search)


@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        full_name = request.form["full_name"].strip()
        email = request.form["email"].strip()
        department = request.form["department"]
        status = request.form["status"]

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Employees (FullName, Email, Department, Status) "
                "VALUES (?, ?, ?, ?)",
                full_name, email, department, status,
            )
            conn.commit()
            flash("Employee added.")
            return redirect(url_for("index"))
        except pyodbc.IntegrityError:
            flash("That email already exists.")
            return redirect(url_for("add_employee"))
        finally:
            conn.close()

    return render_template("form.html", employee=None, title="Add Employee")


@app.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        full_name = request.form["full_name"].strip()
        email = request.form["email"].strip()
        department = request.form["department"]
        status = request.form["status"]
        try:
            cursor.execute(
                "UPDATE Employees SET FullName = ?, Email = ?, Department = ?, "
                "Status = ? WHERE EmployeeId = ?",
                full_name, email, department, status, employee_id,
            )
            conn.commit()
            flash("Employee updated.")
            return redirect(url_for("index"))
        except pyodbc.IntegrityError:
            flash("That email already exists.")
            return redirect(url_for("edit_employee", employee_id=employee_id))
        finally:
            conn.close()

    cursor.execute(f"SELECT {COLUMNS} FROM Employees WHERE EmployeeId = ?", employee_id)
    employee = cursor.fetchone()
    conn.close()
    if employee is None:
        flash("Employee not found.")
        return redirect(url_for("index"))
    return render_template("form.html", employee=employee, title="Edit Employee")


@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Employees WHERE EmployeeId = ?", employee_id)
    conn.commit()
    conn.close()
    flash("Employee deleted.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)