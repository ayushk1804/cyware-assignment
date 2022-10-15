FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y nginx openssl
RUN openssl req -x509 -nodes -days 90 -subj "/C=CA/ST=QC/O=Cyware/CN=assignment.cyware.local" -addext "subjectAltName=DNS:cyware.local" -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt;
RUN apt-get install -y python3 python3-distutils python3-pip
WORKDIR /app
COPY app.py . 
COPY test_app.py . 
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pytest test_app.py | tee /app/pytest.log
CMD ["/bin/bash"]