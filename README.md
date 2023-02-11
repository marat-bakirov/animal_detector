## Installing on a local machine
This project requires python 3.7

### Clone github remote repository
```shell
git clone git@github.com:marat-bakirov/animal_detector.git
```

### Create and activate virtual environment
```shell
cd animal_denector
python3.7 -m venv venv
source venv/bin/activate
```

### Install requirements
```shell
pip install -r requirements.txt
```

#### If there is an error: ModuleNotFoundError: No module named 'tkinter', that may help:

```shell
sudo apt-get install python3-tk
sudo apt-get install python3.7-tk
```

### Run uvicorn server
```shell
uvicorn detector.main:app --reload
```
#### Server default access http://127.0.0.1:8000/object. Swagger doc http://127.0.0.1:8000/docs#/default

## Alternative way to start the server
### Run docker containers with app
```shell
docker-compose -f docker-compose.yml up
```

