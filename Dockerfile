FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /code

RUN apk add --no-cache curl

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "80"]
