FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y libffi-dev libpq-dev curl ca-certificates

# Установка UV
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

COPY ./pyproject.toml pyproject.toml

RUN uv pip install --system --no-cache-dir --upgrade -r pyproject.toml

COPY . .

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]