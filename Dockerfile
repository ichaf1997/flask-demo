FROM 192.168.2.212:8443/library/python:rc-alpine3.12

ENV FLASK_VERSION=1.1.2

RUN pip install flask==$FLASK_VERSION && pip cache purge
COPY *.py /app/
EXPOSE 5000
WORKDIR /app/
CMD ["python", "main.py"]
