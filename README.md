# ecommerce-website
A basic ecommerce website for beginners to learn Django Full Stack Web Development.

To start with this project, first create a virtual environment and install all packages specified in requirements.txt.
Follow the following steps if you are new to the concept of virtual environments in python.

> Install [pip](https://pypi.org/project/pip/)

> Install virtualenv
```bash
pip install virtualenv
```
> Create a virtual environment
```bash
virtualenv ecomm
```
> cd to the folder which contains requirements.txt
```bash
pip install -r requirements.txt
```
> cd to the folder which contains manage.py file and migrate the database to create tables
```bash
python manage.py makemigrations
python manage.py migrate
```
> Run the django server
```bash
python manage.py runserver
```
The application would be running at [localhost:8000](localhost:8000/home/) by default.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
