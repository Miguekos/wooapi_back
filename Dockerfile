FROM    python:3.6

WORKDIR /code

COPY    *.txt /code/

RUN     pip install -r requeriment.txt

COPY    . /code/

#ADD bootstrap.sh /code/
#RUN bash -c "/code/bootstrap.sh"

EXPOSE  8050
#CMD     ["python", "main.py"]