FROM python:3.10

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r /code/requirements.txt --no-cache-dir

COPY . .

CMD . .
