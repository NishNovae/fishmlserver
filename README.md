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
$ sudo docker build -t fishmlserver:<VERSION_NAME> .
$ sudo docker run -d -p --name <PROCESS_NAME> 8877:8765 fishmlserver:<VERSION_NAME>
```

```bash
# execute bash command of docker; connect to CLI
$ sudo docker exec -it <DOCKER_PS_NAME> bash

# exit docker bash
$ exit
```

### Fly.io


