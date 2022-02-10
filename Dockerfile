FROM    python:3.7-slim

WORKDIR /code

COPY    requeriment.txt /code/

RUN     pip install -r requeriment.txt
RUN     mkdir -p logs

COPY    . /code/

#ADD bootstrap.sh /code/
#RUN bash -c "/code/bootstrap.sh"

EXPOSE  8050
#CMD     ["python", "main.py"]