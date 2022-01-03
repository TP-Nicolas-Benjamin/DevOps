FROM python:3.10.1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD app.py /code/

EXPOSE 8080

ENTRYPOINT [ "python", "app.py" ]