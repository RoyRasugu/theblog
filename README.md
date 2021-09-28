# theBlog
## Author

Roy Rasugu 

## Description

This is a flask application that allows writers to post blogs, edit and delite blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person to subscribed to recieve email everytime a new blog is posted by a writer.

## Livepage
hubblog.herokuapp.com/

## User Story
* A user can view the most recent posts.
* Also a user can view and comment the blog posts on the site.
* A user should be able to receive an email alert when a new post is made by joining a subscription.
* Register to be allowed to log in to the application
* A user sees random quotes on the site
* A writer can create a blog from the application and update or delete blogs I have created.

## Dependencies
1. The user will enter the website and will view the blogs available and depending whether they have an account or not they can choose to either sign in or sign up.
2. When one selects signs up they will input their username, email and password. They will then be directed to the login page
3. Once they are in the login page, they will will have to input their correct username and password as registered with so as to be directed to the posted blogs where they can subscribe to the blog or write a blog themselves which will be posted on the site.
4. If one selects the comment button, there is a form where one inputs their comments and after submitting it will be displayed along with the other comments.
5. Subscription, a flash message will say "successfuly subscribed to theBlog"

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/RoyRasugu/theblog.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd theblog
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)


## Contact Information 

You can reach me on my email [royratchizi@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Roy Rasugu**

