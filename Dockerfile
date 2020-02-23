FROM python:3

ENV PYTHONPATH "${PYTHONPATH}:/blurhash"
RUN pip install flask
RUN pip install Pillow
RUN pip install numpy


ADD main.py /

COPY . /

CMD [ "python", "./main.py" ]