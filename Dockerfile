FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y nginx
CMD ["/bin/bash"]