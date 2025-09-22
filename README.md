# Django Student Management System (CRUD)

This project is a full-stack web application built with Python and the Django framework. It serves as a practical demonstration of building a system with complete CRUD (Create, Read, Update, Delete) functionality. The application allows users to manage a database of student records through a clean and simple user interface.

<img src="Home page.png">

## Key Features

-   **Create:** Add new students to the database via a web form.
-   **Read:** Display a list of all students with their details.
-   **Update:** Edit the information of any existing student.
-   **Delete:** Remove students from the database.

## Tech Stack

-   **Backend:** Python, Django
-   **Database:** SQLite 3 (Default)
-   **Frontend:** HTML, CSS (via Django Templates)


## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

-   Python (3.8 or newer)
-   pip (Python package installer)
-   Git

### Installation & Setup

1.  **Clone the repository to your local machine:**

    ```bash
    git clone [https://github.com/modiharsh23/django-StudentDMS-crud.git](https://github.com/modiharsh23/django-StudentDMS-crud.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    This keeps your project's dependencies isolated from other Python projects.

    ```bash
    # Create the virtual environment
    python -m venv env

    # Activate the virtual environment
    # On macOS/Linux:
    source env/bin/activate
    
    # On Windows:
    .\env\Scripts\activate
    ```
    You should see `(env)` at the beginning of your terminal prompt.

3.  **Install the required dependencies:**
    This command reads the `requirements.txt` file and installs all the necessary packages (like Django).

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply the database migrations:**
    This will create the `db.sqlite3` file and set up the necessary database tables.

    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    Your Django application is now ready to go!

    ```bash
    python manage.py runserver
    ```

6.  **View the application:**
    Open your favorite web browser and navigate to:
    
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You should now see the application running!
