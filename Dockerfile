FROM python:3.11

WORKDIR /code

#COPY . /code/

COPY src/fishmlserver/main.py /code/
COPY requirements.txt /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/NishNovae/fishmlserver.git@0.5.0/manifest

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
