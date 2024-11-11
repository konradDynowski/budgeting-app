# Budgeting app - django
The project was about learning the django framework. The main purpose of the application is to have CRUD app for tracking cashflow on a monthly manner, similarly to what I already use with other tools.

## features
The app allows to keep track of the transactions - by typing them in manually. The transaction is described by amount, date, descriptin, and the category. 
Application allows to define categories which are then groupped by groups. 

Besides that, user can plan a monthly budget provided there are defined categories/groups already, by planning a quota for each of the categories. 

On the homepage, user can view transactions for a month, as well as add them.

Another custom feature is ability to import CSV data provided by my bank and prefill a form creating transactions with the information from the statement (it supports only my format, but it's there as a proof of concept)

## installation
1. Navigate to the project directory:
   ```bash
   cd budgeting-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate 
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
## Usage
- Go to `http://127.0.0.1:8000` in your browser to access the app.
- Add, edit, or delete transactions and set budget quotas per category.
- Feel free to migrate categories/groups using the populate_data.py script - it has some test data hardcoded, but You can use it to bulk define your categories
## Technologies Used
- Django
- just a touch of JS
- SQLite

## License
This project is licensed under the MIT License.
