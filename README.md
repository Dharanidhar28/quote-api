# Quote-manager-Api
A simple REST API for managing inspirational quotes using Flask
# Quote Manager (Flask + SQLite)

A simple **Quote Manager web application** built using **Python Flask** and **SQLite**.
The application allows users to **add, view, update, and delete quotes** through a web interface.

This project demonstrates basic **backend development concepts**, including:

* REST API design
* Flask web framework
* SQLite database integration
* CRUD operations
* Frontend and backend interaction

---

## Features

* Add a new quote
* View all quotes
* Update an existing quote
* Delete quotes
* Generate motivational quotes
* Persistent storage using SQLite database

---

## Project Structure

```
quote-api/
│
├── app.py
├── quotes.db
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── script.js
│
└── README.md
```

### File Descriptions

| File                   | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| `app.py`               | Main Flask application containing routes and database logic |
| `quotes.db`            | SQLite database storing quotes                              |
| `templates/index.html` | Web page UI                                                 |
| `static/script.js`     | JavaScript for interacting with the API                     |
| `requirements.txt`     | Python dependencies                                         |

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/quote-manager-api.git
```

Navigate to the project folder:

```
cd quote-manager-api
```

Install dependencies:

```
pip install flask
```

---

## Running the Application

Start the Flask server:

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## API Endpoints

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | `/quotes`         | Get all quotes              |
| POST   | `/quotes`         | Add a new quote             |
| PUT    | `/quotes/<id>`    | Update a quote              |
| DELETE | `/quotes/<id>`    | Delete a quote              |
| GET    | `/generate-quote` | Generate motivational quote |

---

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* JavaScript

---

## Learning Goals

This project was created to practice:

* Backend development using Flask
* API development
* Database operations
* Full-stack communication between frontend and backend

---

## Future Improvements

* Add user authentication
* Improve UI styling
* Add search functionality
* Integrate AI-generated quotes using external APIs

---

## Author

Developed as a learning project for backend development and API design.
