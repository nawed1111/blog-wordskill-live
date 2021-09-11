# WordSkill 

[WordSkill](https://blog-wordskill.herokuapp.com/) is a blog developed using Django framework and postgres. It is hosted in heroku and static files are stored in AWS S3.

## Installation

Clone the project to local machine.
```bash
git clone https://github.com/nawed1111/blog-wordskill-live.git
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install WordSkill.

Install Dependencies
```bash
pip install -r requirements.txt
```
Set Database (Make Sure you are in directory same as manage.py)

```bash
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser
```bash
python manage.py createsuperuser
```
Start a local web server
```bash
python manage. py runserver
```
After successfully running locally, you should be able to access it [localhost:8000](http://127.0.0.1:8000/).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
