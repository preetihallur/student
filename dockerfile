#dockerfile
from python:3.11
workdir /student
copy . .                
cmd ["python","student.py"]
