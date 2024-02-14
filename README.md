The Magic Oven is a web application dedicated to bakery enthusiasts, offering them the opportunity to discover and purchase delicious products, all crafted with love and expertise in a magical oven. With an intuitive and colorful interface, users are invited to explore a wide range of bakery products



![50.png](..%2F..%2F..%2FDesktop%2F50.png)


1. Download and Installation

   Clone this repository locally, into your Python projects folder
   git clone: 
         
         git clone https://github.com/LoredanaTr/Cuptorul-Magic.git

      To install dependencies, run:

          pip install -r requirements.txt


2. Developing a Project Using the Django Framework

   Installation of Django framework - Ensure you have the Django framework installed and run the command below:
   
       pip install django
   
   
   Creating a project using Django - When creating a project, you should use the terminal and run the command below:
   
   
      django-admin startproject project_name


   Creating an application - Before creating the application, navigate to the project directory using the command cd project_name, then run the following command in the terminal:

      python manage.py startapp app_name

   
   After creating the application, go to the settings.py file to configure the application settings and name the database.
   
   Defining models - After defining the database structure models in the models.py file, run the following command:
   

      python manage.py makemigrations
      python manage.py migrate

   Running the application - Use the following command to run the application:
   
      python manage.py runserver

   Creating a superuser - This will help us to access the Django admin interface:
   
      python manage.py createsuperuser