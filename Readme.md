#This is the backend for the e-commerce project I am working on,
I will be listing the step by step instructions I used in the project


1. at first we created the project directory 
2. then git initialized `git init`.
3. after that we created the base file (industry standard) using the bash command `touch Dockerfile docker-compose.yml requirements.txt .env .gitignore`
4. we populated the requirements.txt file with the 4 dependcies mostly used `Django==5.0.2,gunicorn==21.2.0,psycopg[binary]==3.1.18,python-dotenv==1.0.1`
5. since we are using the docker we populated the docker file 
6. `docker compose build`
7. `docker compose run --rm web django-admin startproject config .`

