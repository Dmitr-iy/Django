FROM python:3
LABEL authors="dmitriy"
RUN apt-get update && apt-get upgrade -y

RUN mkdir /practic
COPY . /practic/
WORKDIR /practic

RUN pip install --upgrade pip && pip install django && pip install python-dotenv

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]