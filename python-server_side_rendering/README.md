# Python - Server-Side Rendering

## Description
This project explores server-side rendering in Python using Flask and Jinja2 templating. It covers string templating, dynamic HTML generation, reading data from JSON, CSV, and SQLite sources, and building a multi-page Flask web application.

---

## Requirements
- Python 3.x
- Flask

### Install Flask:
```bash
pip install Flask
```

---

## Project Structure
```
python-server_side_rendering/
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── template.txt
├── items.json
├── products.json
├── products.csv
├── create_db.py
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    └── product_display.html
```

---

## Tasks

### 0. Creating a Simple Templating Program
**File:** `task_00_intro.py`

Generates personalized invitation files from a template with placeholders and a list of attendees. Output files are named `output_1.txt`, `output_2.txt`, etc.

**Run:**
```bash
python main_00.py
```

**Features:**
- String placeholder replacement
- Handles missing values with `N/A`
- Input validation and error handling
- Empty template and empty list detection

---

### 1. Creating a Basic HTML Template in Flask
**File:** `task_01_jinja.py`

A basic Flask application with multiple pages using reusable Jinja templates for header and footer.

**Run:**
```bash
python task_01_jinja.py
```

**Routes:**
| URL | Page |
|-----|------|
| `http://localhost:5000/` | Home |
| `http://localhost:5000/about` | About |
| `http://localhost:5000/contact` | Contact |

---

### 2. Dynamic Template with Loops and Conditions
**File:** `task_02_logic.py`

Extends the Flask app to display a dynamic list of items read from a JSON file, using Jinja loops and conditional statements.

**Run:**
```bash
python task_02_logic.py
```

**Routes:**
| URL | Page |
|-----|------|
| `http://localhost:5000/items` | Items List |

---

### 3. Displaying Data from JSON or CSV Files
**File:** `task_03_files.py`

Reads and displays product data from JSON or CSV files based on a `source` query parameter. Supports optional filtering by `id`.

**Run:**
```bash
python task_03_files.py
```

**Routes:**
| URL | Description |
|-----|-------------|
| `http://localhost:5000/products?source=json` | All products from JSON |
| `http://localhost:5000/products?source=csv` | All products from CSV |
| `http://localhost:5000/products?source=json&id=1` | Filter by ID |
| `http://localhost:5000/products?source=xml` | Error: Wrong source |

---

### 4. Extending Data Display to Include SQLite
**File:** `task_04_db.py`

Extends Task 3 to also support SQLite as a data source using `source=sql`.

**Run:**
```bash
python create_db.py
python task_04_db.py
```
> **Note:** Run `create_db.py` only once to create and populate the database.

**Routes:**
| URL | Description |
|-----|-------------|
| `http://localhost:5000/products?source=sql` | All products from SQLite |
| `http://localhost:5000/products?source=sql&id=1` | Filter by ID from SQLite |

---

## Author
- Holberton School Student