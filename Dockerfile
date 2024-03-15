FROM python:3.9-slim-buster
WORKDIR /microapp
COPY . /microapp
COPY Pipfile ./
RUN pip3 install pipenv
RUN pipenv install
EXPOSE 8080
# If Pipenv is not able to be used on local server
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#CMD ["waitress-serve", "--host 127.0.0.1", "app:app"]
ENTRYPOINT ["sh", "-c", "cd /microapp && pipenv shell && waitress-serve app:app"]
