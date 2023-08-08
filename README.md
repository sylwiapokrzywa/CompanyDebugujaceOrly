Welcome to the Django Firm API project named "CompanyDebugujaceOrly"! This project was created for learning purposes of building an API using the Django framework
and getting familiar with containerization technology using Docker. The project enables storing data about companies, their addresses, and opening hours.
This project serves as an example of implementing a simple Django API that allows adding, editing, deleting, and retrieving information about companies along 
with their addresses and opening hours. It utilizes basic Django ORM functionalities for managing data in the database.

=================================================================================================================================================================
Installation

1. Clone the repository to your local computer:

git clone https://github.com/sylwiapokrzywa/CompanyDebugujaceOrly

2. Go to the project directory:

cd CompanyDebugujaceOrly

3. Create and activate the virtual environment:

python -m venv venv
source venv/bin/activate

4. Install required dependencies:

pip install -r requirements.txt

5. Perform database migrations:

python manage.py migrate

6. Start the development server:

python manage.py runserver

7. The application will be available at http://localhost:8000/.
