# Documentation:
Running process 
- create repo locally:
```
git init
```
- clone the repository:
```
git remote add origin git@github.com:MikeYeromenko/test-task.git
```
- pull repo:
```
git pull origin master
```
- create virtual env and add dependencies
```
poetry install
```
- activate environment
```
poetry shell
```
- run server:
```
python main.py
```
- go and test:
```http://127.0.0.1:8000/docs```