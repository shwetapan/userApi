# Problem Statement Description
Develop an API endpoint to get a list of users.

# Solution
django rest framework has been used to build the api.

#### Run locally
Clone the repo and cd into users folder

```
pip3 install -r requirements.txt

python manage.py runserver

Now, Open this link in your browser...  
http://127.0.0.1:8000/

To get the api documentation, open this link in your browser 
http://127.0.0.1:8000/swagger

```

#### Deployed link
https://getuserlist.herokuapp.com/

#### documentation

https://getuserlist.herokuapp.com/swagger/



#### Run within docker

Run the image and bash into it to start the server
docker run python-django


# API

### Get paginated users result
GET `/`

### Specify a page

GET `?offset=40`

### Filter users

Filter fields:

- id

Example:

GET


/?id=6
/?id=1000

