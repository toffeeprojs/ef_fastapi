FROM python:3.13.5-alpine3.22

WORKDIR /code

RUN apk add --no-cache curl

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src/main:app", "--host", "0.0.0.0", "--port", "8000"]
