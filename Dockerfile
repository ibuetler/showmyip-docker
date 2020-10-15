FROM hackinglab/alpine-python-flask:3.1.0

MAINTAINER Ivan Bütler <ivan.buetler@compass-security.com>

# Install app requirements (keep separate from other files to allow quicker build times)
ADD root/app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

ADD root /
