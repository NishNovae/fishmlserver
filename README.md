# fishmlserver

### Deploy
![image](https://github.com/user-attachments/assets/a73f0819-66a6-4e80-830b-a2d0bff2dcc7)

### Run
- dev
- http://localhost:8000/docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserver.main:app --reload
```

- prd
- http://localhost:8000/docs
```bash
$ uvicorn src.fishmlserver.main:app --host 0.0.0.0 --port 8949
```

### Docker
```bash
$ sudo docker build -t fishmlserver:0.2.0 .
$ sudo docker run -d --name fmlserv-020 -p 8877:8765 fishmlserver:0.2.0
```
