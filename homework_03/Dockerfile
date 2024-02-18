# Для сбора образа использовать sudo docker build . -t myfastapp
# Для запуска контейнера использовать sudo docker run -it -p 8000:8000 myfastapp

FROM python:3.9-buster
WORKDIR /myapp

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY fastapi_app.py ./
EXPOSE 8000
CMD ["uvicorn", "fastapi_app:app", "--host=0.0.0.0","--port=8000"]
