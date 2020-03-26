FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
WORKDIR /app
RUN apt-get update && apt-get install -y \
    python-pip

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN pip install uvicorn
RUN python setup.py sdist

