# How to set up development environment

install requirements 
```
pip install -r requirements.txt
```
start flask server
```
cd Backend && python -m flask run
```

### hot module reload
`FLASK_APP=app.py FLASK_ENV=development flask run`

### total length of lines in code
`git ls-files | xargs wc -l`