FROM python:3.9.18-alpine

RUN mkdir -p /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# COPY requirements.txt ./

COPY . .

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install --upgrade pip  

RUN pip install -r requirements.txt 
RUN apk del .tmp

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
