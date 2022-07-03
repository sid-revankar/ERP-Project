# ERP Software For Educational Institutions

The main objective of this project is to provide an ERP software for managing an educational institution.




## Features

#### Student Portal
- Student Feedback
- Student Result

#### Staff Portal
- Student Details
- Attendance Management
- Feedback Management
- Result Management



## Installation

~ To run this project locally

### Pre-requisites

- Python v3.8+
- Django v4.0+

### Creating an environment
1. Create a Folder where you want to save the project

2. Create a Virtual Environment and Activate

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```


Install remaining dependencies by downloading the [requirements.txt](https://raw.githubusercontent.com/sid-revankar/ERP-Project/master/requirements.txt) file and running the following command

```
$  pip install -r requirements.txt
```

### Running the Application

1. Clone this project
```
$  git clone https://github.com/sid-revankar/ERP-Project.git
```

2. cd into the project directory
```
$  cd ERP-Project
```

3. Now make migrations
```
$  python manage.py makemigrations
$  python manage.py migrate
```

4. Create superuser to login
```
$  python manage.py createsuperuser
```
Then add your desired email, username and password.

5. Then run the server
```
$  python manage.py runserver
```

#### This project is still in development and we are open to suggestions and changes. 


## Authors

- [@sidrevankar](https://github.com/sid-revankar)
- [@SpoodoW](https://github.com/SpoodoW)
- [@gauravhegade](https://github.com/gauravhegade)
