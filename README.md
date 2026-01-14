# Image Processing Platform API

Backend for image processing and transformation service, it is inspired by platforms such as Cloudinary and iLoveIMG. Allow users to authenticate, upload images, apply various transformations, and retrieve images in different formats.

# Main Features

## Authentication

- Sign up
- Login
- JWT Authentication-based
- Protected Endpoints

## Image Management 

  - Upload Images
  - Retrieve Images
  - Delete Images

## Image Transformation
  - Compress
  - Apply Filters
  - Change Format

## Stack Used

- Python 3.12.4
- Django
- Django Rest Framework
- Simple JWT
- Pillow
- PostgreSQL
- Docker

## How to run the project

***Note***: *Docker and Docker compose are required*

### Clone the repository

```bash
git https://github.com/miguellozano03/image_processing_platform.git
cd image_processing_platform
```

### Build and start the containers

```bash
docker compose build --no-cache
docker compose up
```

### Run database migrations
```bash
docker compose exec web python manage.py migrate
```

### (Optional) Create a superuser

```bash
docker compose exec web python manage.py createsuperuser
```

### The API will be able at:

```
http://localhost:8000/
```