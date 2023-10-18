# EngenAI Test Task

<img width="512" alt="Screenshot 2023-10-18 at 20 27 11" src="https://github.com/winterfriz/engenai-test-task/assets/12971836/75612735-2779-4640-8a83-3b4818fc0fce">


## Installation

### Postgres Database

Install postgres database any convinient way. 

Create a database, for example, named `engenai_test_task`.

Enable the extension (do this once in each database where you want to use it):  
`CREATE EXTENSION vector;`. 

If errors appear, install pgvector, see [pgvector installation](https://github.com/pgvector/pgvector#installation).

### Django

Install the project's dependencies using Pipenv:  
`pipenv install`

Activate the Virtual Environment:  
`pipenv shell`

Set up environment, create a .env file, and populate it with data: 
```
# secret keys
SECRET_KEY=''  # Django secret key
OPENAI_API_KEY=''

# postgres database
DB_USER=''
DB_NAME=''
DB_PASSWORD=''
DB_PORT=''
```

Apply migrations to the database:  
`python manage.py migrate`

## Getting Started

Run the project:
`python manage.py runserver`

🎉
 
