  1 FROM python:3.7
  2 
  3 RUN apt-get update
  4 RUN apt-get install -y build-essential python-dev git
  5 
  6 RUN pip3 install --upgrade pip setuptools
  7 RUN pip3 install requests-futures
  8 RUN pip3 install lxml
  9 RUN pip3 install fake-useragent
 10 RUN pip3 install git+https://github.com/jhylands/recipe-scrapers.git
 11 
 12 CMD ["python3"]


