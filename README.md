# 🧑‍💻 User Management System (Flask + MySQL)

A simple User Management System built using Flask and MySQL. This project allows users to register, login, and access a dashboard after authentication.
---
## Features
* User Registration system
* Login Authentication
* Dashboard after successful login
* MySQL Database integration
* Clean UI using HTML & CSS
---

## 🛠️ Tech Stack
* Python (Flask)
* MySQL
* HTML
* CSS
* Jinja Templates
---
##  Project Structure
```
UMS/
│── app.py
│── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│── static/
│   ├── style.css
```
---
##  Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/hemantgoswami-24/ums-flask-project.git
cd ums-flask-project
```
---
### 2. Install dependencies
```
pip install flask mysql-connector-python
```
---
### 3. Setup MySQL Database
* Create database:
```
CREATE DATABASE ums;
```
* Use database:
```
USE ums;
```
* Create table:
```
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);
```
---
### 4. Run the project
```
python app.py
```
---
### 5. Open in browser
```
http://127.0.0.1:5000/ 
## 📌 Future Improvements
* Password hashing (security)
* JWT Authentication
* Logout functionality
* REST API version
---
## 🙌 Author
**Hemant Giri**
