# Django Blog — Coursework Project

_Author: Natalia Tsvietukhina_

_Course: WEB Advanced Programming (2024/2025)_

A fully functional Django Blog Application created as a coursework project.
The application demonstrates understanding of Django fundamentals, including models, views, templates, authentication, CRUD operations, media file uploads, and authorization rules.

## Features Overview
**Posts (CRUD)**
- Create posts (only for logged-in users)
- View all posts on the homepage
- View detailed post information
- Edit posts (only the post author)
- Delete posts (only the post author)
- Image upload support (saved in /media/posts/)
- Search posts by title or body content

**Comments System**

- Add comments to any post (only for logged-in users)
- Display: comment text/author/creation date
- Delete comments (only by comment author)
- Comments linked to posts using ForeignKey

**User Authentication**

- User Registration
- User Login / Logout

**Only logged-in users can:**

- Create posts
- Add comments
- Edit/delete their own posts
- Delete their own comments
- Dynamic navigation bar displaying user status

**UI & Templates**

- Responsive design using Bootstrap
- Template inheritance via base.html
- Simple and intuitive forms for posts and comments

## Project Structure

```Blog/
│
├── blog/                 # Django project settings & root
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/                # Uploaded images
│
├── posts/                # Blog posts app
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   └── posts/
│   │       ├── edit_post.html
│   │       ├── post_detail.html
│   │       ├── posts.html
│   │       
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Post & Comment models
│   ├── tests.py
│   ├── urls.py
│   └── views.py          # CRUD logic + commenting
│
├── users/                # Authentication app
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       └── register.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py          # Register, Login, Logout
│
├── .gitignore
├── db.sqlite3            (ignored by Git)
└── manage.py
``` 

## Installation & Setup

1. Clone the repository
git clone https://github.com/Tsvietukhina/Django-blog.git
cd Django-blog
2. Install dependencies
pip install django pillow
3. Apply migrations
python manage.py migrate
4. Run the development server
python manage.py runserver
5. Open in browser  http://127.0.0.1:8000/

## Usage Instructions
- Register a new user - _/users/register/_
- Log in - _/users/login/_
- Create a post - _Available on the homepage (only when logged in)_
- View a post - _Click “View details”_
- Comment on a post - _Comment form appears under each post (only when logged in)_
- Edit/Delete post - _Buttons appear only for the post author_
- Delete your comment - _Visible only on comments authored by the logged-in user_

## Technologies Used

- Python 3.11
- Django 5
- Bootstrap 4
- SQLite
- Git & GitHub

## Conclusion

This Django Blog project demonstrates strong understanding of:

- MVC/MVT structure
- Routing
- Template rendering
- Database modeling
- CRUD logic
- Authentication & permissions
- Bootstrap front-end integration

The application is functional, clean, and follows good coding practices.
