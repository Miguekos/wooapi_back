FROM    python:3.6

WORKDIR /code

COPY    *.py /code/
COPY    *.txt /code/

RUN     pip install -r requeriment.txt

#ADD bootstrap.sh /code/
#RUN bash -c "/code/bootstrap.sh"

EXPOSE  6000
#CMD     ["python", "main.py"]