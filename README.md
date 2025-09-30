# Django Blog Website - Setup and Usage Guide

This guide will walk you through downloading, setting up, and using the Django blog website from the GitHub repository.

## Repository Information
- **Repository URL**: https://github.com/MossaJehad/django-blog-website
- **Project Type**: Django Web Application
- **Python Version**: 3.13

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Download and Setup](#download-and-setup)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Using the Blog](#using-the-blog)
6. [Admin Panel](#admin-panel)
7. [Project Structure](#project-structure)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.13 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **pip** (usually comes with Python)
- **pipenv** (optional but recommended) - Install with `pip install pipenv`

## Download and Setup

### Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/MossaJehad/django-blog-website.git
```

### Step 2: Navigate to the Project Directory

```bash
cd django-blog-website
```

## Installation

### Option 1: Using Pipenv (Recommended)

1. Install pipenv if you haven't already:
   ```bash
   pip install pipenv
   ```

2. Install dependencies and create virtual environment:
   ```bash
   pipenv install django
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

### Option 2: Using pip and venv

1. Create a virtual environment:
   ```bash
   python -m venv blog_env
   ```

2. Activate the virtual environment:
   - **Windows**: `blog_env\Scripts\activate`
   - **macOS/Linux**: `source blog_env/bin/activate`

3. Install Django:
   ```bash
   pip install django
   ```

## Running the Application

### Step 1: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 2: Create a Superuser (Optional but Recommended)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 3: Start the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## Using the Blog

### Accessing the Website

1. Open your web browser
2. Navigate to `http://127.0.0.1:8000/`
3. You'll see the blog homepage

### User Registration and Login

1. **Sign Up**: Click on "Sign Up" to create a new account
2. **Login**: Use the "Log In" link to access existing accounts
3. **Logout**: Click "Log Out" when you're done

### Blog Features

#### For Regular Users:
- **View Posts**: Browse all blog posts on the homepage
- **Read Posts**: Click on any post title to read the full content
- **User Authentication**: Register and login to access additional features

#### For Logged-in Users:
- **Create Posts**: Write new blog posts
- **Edit Posts**: Modify your own posts
- **Delete Posts**: Remove your own posts

### Navigation

- **Home**: View all blog posts
- **+ New Post**: Create a new blog post (requires login)
- **Post Details**: Click on any post to view full content
- **Edit/Delete**: Available for your own posts when logged in

## Admin Panel

### Accessing the Admin Panel

1. Ensure you've created a superuser (see Step 2 in Running the Application)
2. Navigate to `http://127.0.0.1:8000/admin/`
3. Login with your superuser credentials

### Admin Features

- **User Management**: View and manage user accounts
- **Post Management**: Create, edit, and delete any blog posts
- **Content Moderation**: Full control over all blog content

## Project Structure

```
django-blog-website/
├── manage.py				# Django management script
├── db.sqlite3				# SQLite database file
├── Pipfile					# Pipenv dependencies
├── HOW_TO_USE_BLOG.md		# This instruction file
├── blog_project/			# Main project settings
│   ├── settings.py			# Django settings
│   ├── urls.py				# Main URL configuration
│   └── wsgi.py				# WSGI configuration
├── blog/					# Blog application
│   ├── models.py			# Blog post model
│   ├── views.py			# Blog views
│   ├── urls.py				# Blog URL patterns
│   └── admin.py			# Admin configuration
├── accounts/				# User authentication app
│   ├── views.py			# Authentication views
│   └── urls.py				# Authentication URLs
├── templates/				# HTML templates
│   ├── base.html			# Base template
│   ├── home.html			# Homepage
│   ├── post_details.html	# Post detail view
│   ├── post_new.html		# Create post form
│   ├── post_edit.html		# Edit post form
│   ├── post_delete.html	# Delete confirmation
│   ├── signup.html			# User registration
│   └── registration/
│       └── login.html		# Login form
└── static/					# Static files (CSS, images)
    └── css/
        └── base.css		# Styling
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   python manage.py runserver 8001
   ```
   Use a different port if 8000 is occupied.

2. **Migration Errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic
   ```

4. **Permission Errors**
   - Ensure you're in the correct directory
   - Check that your virtual environment is activated

### Getting Help

- Check the Django documentation: https://docs.djangoproject.com/
- Review error messages in the terminal
- Ensure all dependencies are installed correctly

## Features Overview

### Blog Functionality
- **CRUD Operations**: Create, Read, Update, Delete blog posts
- **User Authentication**: Registration, login, logout
- **Responsive Design**: Works on desktop and mobile devices
- **Admin Interface**: Full administrative control

### Technical Features
- **Django Framework**: Modern Python web framework
- **SQLite Database**: Lightweight database for development
- **Template System**: Dynamic HTML generation
- **Static Files**: CSS styling and potential for media files
- **URL Routing**: Clean and organized URL patterns

## Next Steps

After setting up the blog, you can:

1. **Customize the Design**: Modify CSS files in the `static/css/` directory
2. **Add Features**: Extend functionality by modifying models and views
3. **Deploy**: Consider deploying to platforms like Heroku, PythonAnywhere, or DigitalOcean
4. **Database**: Switch to PostgreSQL or MySQL for production use

---

**Enjoy your Django blog website!** 🎉

For any issues or questions, please refer to the Django documentation or create an issue on the GitHub repository.