FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y nginx openssl
RUN openssl req -x509 -nodes -days 90 -subj "/C=CA/ST=QC/O=Cyware/CN=assignment.cyware.local" -addext "subjectAltName=DNS:cyware.local" -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt;
CMD ["/bin/bash"]