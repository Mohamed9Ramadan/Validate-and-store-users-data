from flask import Flask, request, render_template
import re
import hashlib
import json
import csv
import os

app = Flask(__name__)
users = []

def validate_name(name):
    pattern = r'^[a-zA-Z]+$'
    return bool(re.match(pattern, name))

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_password(password):
    if (len(password) >= 8 and 
        re.search(r'[A-Z]', password) and 
        re.search(r'[a-z]', password) and 
        re.search(r'\d', password) and 
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return True
    return False

def save_to_file(data):
    with open('users.json', 'w') as f:
        json.dump(data, f)
    
    csv_file_path = 'users.csv'
    file_exists = os.path.isfile(csv_file_path)

    with open(csv_file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if not file_exists:
            csv_writer.writerow(data[0].keys())
        csv_writer.writerow(data[-1].values())

def load_from_file():
    with open('users.json', 'r') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        
        if not validate_name(first_name):
            return "Enter a valid first name (only letters)."
        if not validate_name(last_name):
            return "Enter a valid last name (only letters)."
        if not validate_email(email):
            return "Enter a valid email (example@example.example)."
        if not validate_password(password):
            return "Enter a valid password (at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character)."
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = {"first_name": first_name, "last_name": last_name, "email": email, "pass": hashed_password}
        users.append(user_data)
        save_to_file(users)
        return "Sign-up finished successfully!"
    
    return render_template('signup.html')

@app.route('/users')
def show_users():
    users = load_from_file()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)