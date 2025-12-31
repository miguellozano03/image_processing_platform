FROM python:3.12.4-slim
 
RUN mkdir /app
 
WORKDIR /app
 
ENV PYTHONUNBUFFERED=1 

RUN pip install --upgrade pip
 
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libtiff-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev tk8.6-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    git \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt  /app/ 
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app/
 
EXPOSE 8000
 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
