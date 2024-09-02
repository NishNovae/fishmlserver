FROM python:3.11.9-alpine3.20

WORKDIR /code

#COPY . /code/

COPY src/fishmlserver/main.py /code/
COPY requirements.txt /code/

RUN pip install git+https://github.com/NishNovae/fishmlserver.git/0.3.0/fish

CMD ["uvicorn", "src.fishmlserver.main:app", "--host", "0.0.0.0", "--port", "8080"]
