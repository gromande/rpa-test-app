from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
import os
import csv
from io import StringIO

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Hardcoded credentials
ADMIN_USERNAME = 'Admin'
ADMIN_PASSWORD = 'Admin123'

# Dummy user data for reports
USERS_DATA = [
    {'username': 'Admin', 'first_name': 'Administrator', 'last_name': 'User', 'role': 'Administrator'},
    {'username': 'john_doe', 'first_name': 'John', 'last_name': 'Doe', 'role': 'Manager'},
    {'username': 'jane_smith', 'first_name': 'Jane', 'last_name': 'Smith', 'role': 'Employee'},
    {'username': 'bob_wilson', 'first_name': 'Bob', 'last_name': 'Wilson', 'role': 'Employee'},
    {'username': 'alice_brown', 'first_name': 'Alice', 'last_name': 'Brown', 'role': 'Supervisor'}
]

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('landing.html', username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Find user data for the logged-in user
    user_data = next((user for user in USERS_DATA if user['username'] == session['username']), None)
    return render_template('profile.html', user=user_data)

@app.route('/reports')
def reports():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('reports.html', users=USERS_DATA)

@app.route('/download_users_csv')
def download_users_csv():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Create CSV content
    output = StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['Username', 'First Name', 'Last Name', 'User Role'])
    
    # Write data rows
    for user in USERS_DATA:
        writer.writerow([user['username'], user['first_name'], user['last_name'], user['role']])
    
    # Create response
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=users_report.csv'
    
    return response

if __name__ == '__main__':
    app.run(debug=True)