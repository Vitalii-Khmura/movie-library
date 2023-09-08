# Movie library project

Django project for searching movie and genres



## Instalation

Python3 must be already installed

```shell
git clone https://github.com/Vitalii-Khmura/movie-library.git
cd movie_library
python -m venv venv
venv/Scripts/activate
pip innstall requirements.txt

python manage.py runserver
```

Then you should create an ```.env``` file and enter in this file ```SECRET_KEY```

```shell
    SECRET_KEY=your_secret_key
```

All Environment variables that should be in .env file are specified in the .env_sample file

## Features

* Authentication functionality for User
* Searching movie & genres directly from website
* Detailed information about each film


## Demo
![Website interface](demo.png)

