FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install postgresql-client -y

COPY . /app/

RUN pip3 install -r requirements.txt

EXPOSE 3080
CMD ["python3", "main.py"]