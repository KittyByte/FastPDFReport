FROM python:3.12

WORKDIR /project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libffi-dev libpq-dev curl ca-certificates

# Установка UV
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

COPY ./pyproject.toml pyproject.toml

RUN uv pip install --system --no-cache-dir --upgrade -r pyproject.toml

COPY . .

ENTRYPOINT ["./entrypoint.sh"]