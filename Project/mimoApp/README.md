# Author 
-Kevin Estiven Lozano Duarte 20221020152
# MimoApp

MimoApp is a modern web application designed to manage courses, lessons, and user enrollments. It includes features like user authentication, course creation, lesson management, and enrollment management. Built using FastAPI, SQLAlchemy, PostgreSQL, and Docker, this application follows a microservice architecture and leverages design patterns to ensure maintainability and scalability.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Directory Structure](#directory-structure)
- [API Documentation](#api-documentation)
- [Running the Application](#running-the-application)
- [Database Schema](#database-schema)
- [Authentication](#authentication)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

MimoApp is an educational platform that allows users to register, create, and manage courses and lessons. It features:
- User authentication and management.
- Course and lesson management.
- User enrollments in courses.
- A clean and modern frontend built using responsive design.

## Features

- **User Registration & Login**: Users can sign up, log in, and manage their accounts.
- **Course Management**: Admins can create courses with titles and descriptions.
- **Lesson Management**: Admins can add lessons to courses with a title and content.
- **Enrollment Management**: Users can enroll in courses, and their progress can be tracked.
- **API Integration**: The system provides RESTful APIs for interacting with courses, lessons, and users.

## Technologies Used

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: Bcrypt
- **Docker**: For containerization
- **Pydantic**: Data validation
- **OAuth2**: For authentication with token-based security

