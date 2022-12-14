FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y nginx openssl
RUN openssl req -x509 -nodes -days 90 -subj "/C=CA/ST=QC/O=Cyware/CN=assignment.cyware.local" -addext "subjectAltName=DNS:cyware.local" -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt;
COPY nginx/self-signed.conf /etc/nginx/snippets/self-signed.conf
COPY nginx/aayush-app.conf /etc/nginx/sites-available
RUN chown root:root /etc/nginx/snippets/self-signed.conf
RUN chown root:root /etc/nginx/sites-available/aayush-app.conf
RUN ln -sf /etc/nginx/sites-available/aayush-app.conf /etc/nginx/sites-enabled/aayush-app.conf
RUN apt-get install -y python3 python3-distutils python3-pip
RUN rm -rf /etc/nginx/sites-enabled/default
WORKDIR /app
COPY webapp/app.py . 
COPY webapp/test_app.py . 
COPY webapp/requirements.txt .
RUN pip install -r requirements.txt
RUN pytest test_app.py | tee /app/pytest.log
RUN nginx -t
COPY entrypoint.sh .
RUN chmod a+x entrypoint.sh
CMD [ "./entrypoint.sh" ]