FROM python:3.13.5-alpine3.22

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["fastapi", "run", "src/main.py", "--proxy-headers", "--port", "80"]
