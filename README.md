# 🔐 Secure Login System

A secure login web application built with Python and Flask. The project demonstrates user registration, secure password hashing, input validation, session management, logout functionality, and protection against SQL injection.

## 🚀 Features

* User registration
* User login and logout
* Secure password hashing using bcrypt
* Password confirmation
* Basic input validation
* Session-based authentication
* Protected user dashboard
* SQLite database
* Parameterized SQL queries
* SQL injection protection
* Duplicate username and email protection
* Clean and responsive user interface

## 🛠️ Technologies Used

* Python
* Flask
* SQLite
* bcrypt
* HTML5
* CSS3

## 📁 Project Structure

```text
Secure-Login-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── users.db
│
├── static/
│   └── style.css
│
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

> `database/users.db` is generated automatically when the application runs and is excluded from Git using `.gitignore`.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/pranav-gholap/Secure-Login-System.git
```

### 2. Open the project

```bash
cd Secure-Login-System
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
myenv\Scripts\activate
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask server:

```powershell
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔒 Security Features

### Password Hashing

Passwords are never stored as plain text. The application uses bcrypt to securely hash passwords before storing them in the database.

### SQL Injection Protection

Database queries use parameterized SQL statements instead of directly inserting user input into SQL queries.

### Session Management

Flask sessions are used to maintain authenticated users. The dashboard cannot be accessed without a valid login session.

### Input Validation

The application checks usernames, email addresses, passwords, and password confirmation before creating an account.

### Logout

Users can securely end their session using the logout function.

## 🧪 Testing

The application was tested for:

* Successful user registration
* Successful login
* Invalid login credentials
* Password length validation
* Password confirmation validation
* Duplicate username/email registration
* Logout functionality
* Unauthorized dashboard access
* SQL injection protection

## 📸 Screenshots

Screenshots of the application can be added here after testing:

1. Registration page
2. Login page
3. Dashboard
4. Logout/login validation
5. Security testing

## 🔮 Future Improvements

* Two-Factor Authentication (2FA)
* Email verification
* Password reset functionality
* Account lockout/rate limiting
* CSRF protection
* Stronger password policy
* Production deployment with HTTPS

## 👨‍💻 Author

**Pranav Gholap**

Information Technology Student

## 📄 License

This project is created for educational and internship purposes.
