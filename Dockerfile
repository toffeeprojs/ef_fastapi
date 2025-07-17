FROM ghcr.io/astral-sh/uv:python3.13-alpine

ENV PORT=8000
ENV WORKERS=4
ENV ROOT_PATH="/api/v1"

RUN apk add --no-cache curl

WORKDIR /code

RUN apk add --no-cache --virtual .build-deps \
        build-base \
        python3-dev

COPY uv.lock pyproject.toml ./
COPY src/common_lib src/common_lib
RUN uv sync --compile-bytecode --locked --no-install-project

RUN apk del .build-deps

COPY src src
RUN uv sync --locked

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD ["/bin/sh", "-c", "curl -f http://localhost:${PORT}/health || exit 1"]

CMD ["/bin/sh", "-c", "uv run fastapi run src/main.py --proxy-headers --port ${PORT} --workers ${WORKERS} --root-path ${ROOT_PATH}"]
