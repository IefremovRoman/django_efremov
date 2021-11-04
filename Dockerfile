# syntax=docker/dockerfile:1
FROM python:3.9.7
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# RUN apk add --update --no-cache g++ gcc libxslt-dev libxml2-dev postgresql-dev python3-dev
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
#CMD ["python", "manage.py"]
# ENV DJANGO_DEBUG=True
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]