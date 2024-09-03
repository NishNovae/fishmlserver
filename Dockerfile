#FROM python:3.11
FROM datamario24/python311scikitlearn-fastapi:1.0.0

WORKDIR /code

#COPY . /code/

COPY src/fishmlserver/main.py /code
#COPY requirements.txt /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/NishNovae/fishmlserver.git@0.7.0/path

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
