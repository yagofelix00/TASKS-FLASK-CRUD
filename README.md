# 📝 Flask Tasks API

A simple RESTful API built with **Flask** to manage tasks using an in-memory data structure.  
This project implements a full **CRUD (Create, Read, Update, Delete)** flow and is ideal for learning and practicing REST APIs with Python.

---

## 📌 Project Overview

The **Flask Tasks API** allows users to create, retrieve, update, and delete tasks through HTTP requests.  
Tasks are stored in memory (Python list), making the project lightweight and easy to run without external dependencies such as databases.

This project focuses on:
- REST principles  
- Request/response handling  
- JSON data exchange  
- API endpoint design  

---

## 🚀 Features

### 🧩 Task Management (CRUD)
- Create a new task  
- List all tasks  
- Retrieve a task by ID  
- Update task data  
- Delete a task  

### ⚙️ API Behavior
- JSON-based communication  
- Auto-increment task IDs  
- Proper HTTP status codes (`200`, `404`)  
- Clear success and error messages  

---

## 📂 Project Structure

```

flask-tasks-api/
│
├── app.py
├── models/
│   └── task.py
│
└── README.md

````

---

## 🔗 API Endpoints

### ➕ Create Task
**POST** `/tasks`

```json
{
  "title": "Study Flask",
  "description": "Learn how to build REST APIs",
  "completed": false
}
````

---

### 📋 Get All Tasks

**GET** `/tasks`

Response example:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Study Flask",
      "description": "Learn how to build REST APIs",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

---

### 🔍 Get Task by ID

**GET** `/tasks/<id>`

---

### ✏️ Update Task

**PUT** `/tasks/<id>`

```json
{
  "title": "Study Flask API",
  "description": "CRUD with Flask",
  "completed": true
}
```

---

### ❌ Delete Task

**DELETE** `/tasks/<id>`

---

## 🖼️ Output Example

API tested using **Postman**, returning JSON responses for both successful and error scenarios.

*(You may include a screenshot of a Postman request here)*

```
POST /tasks → 200 OK
GET /tasks → 200 OK
GET /tasks/99 → 404 Not Found
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/flask-tasks-api.git
cd flask-tasks-api
```

### 2️⃣ Install dependencies

```bash
pip install flask
```

### 3️⃣ Run the application

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask**
* **Postman** (for API testing)
* **JSON**

---

## 📝 Notes

* Tasks are stored **in memory** and will be lost when the server restarts.
* This project is intended for **learning purposes**.
* No database is used in this version.

---

## 🔮 Future Improvements

* Persist data using a database (SQLite / PostgreSQL)
* Add data validation
* Implement authentication
* Add pagination
* Add automated tests
* Dockerize the application

---

## 👨‍💻 Author

**Yago Félix**  
💼 Python Developer — Back-end | Data Analysis | Automation  
🔍 Focused on building APIs, automated solutions, and data pipelines using Python.  
🔗 GitHub: [https://github.com/yagofelix00](https://github.com/yagofelix00)

---
