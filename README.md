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
