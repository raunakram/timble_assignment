1> First delete the db.sqlite file
2> in cmd Run: python manage.py makemigrations
3> in cmd Run: python manage.py migrate
4> in cmd Run: python manage.py runserver
5> Now create user:
 i> goto postman 
 ii> hit this url: http://127.0.0.1:8000/api/register/
 iii> create a user, write in body part in JSON format: {"email": "user@example.com", "password": "password123", "full_name": "John Doe"}


To login:
1> hit this url: http://127.0.0.1:8000/api/login/
2> in body part, in JSON format write like this:
{
    "email": "user@example.com",
    "password": "password123"
}
3> Copy the access token we use it for further  




Store movie data form TMDb:
1> Hit this url it will automatically store the data: http://127.0.0.1:8000/movies/fetch-movies/



To Post Reviews:
To create a review: 
1> Goto: http://127.0.0.1:8000/movies/reviews/
2> Authorization: paste asscess token
3> Use post method
4> in body part in JSON format paste like this:
{
    "movie": 4,
    "rating": 5,
    "comment": "This movie was fantastic! Highly recommended.",
    "user": 1
}



To Get:
go to this url:
http://127.0.0.1:8000/movies/reviews/




To update:
use patch in postman:
http://127.0.0.1:8000/movies/reviews/2/
{
    "rating": 45,
    "comment": "Updated comment"
}


To Delete:
Goto this url
http://127.0.0.1:8000/movies/reviews/2/


To filter:
use get method
use like this:
http://127.0.0.1:8000/movies/reviews?genre=Action



For pagination:
http://127.0.0.1:8000/movies/reviews/?page=2






