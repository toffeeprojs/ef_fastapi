FROM ghcr.io/astral-sh/uv:python3.13-alpine

ENV PORT 8000

RUN apk add --no-cache curl

WORKDIR /code

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY src .

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${PORT}/health || exit 1

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
