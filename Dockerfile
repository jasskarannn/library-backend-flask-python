FROM python:3.9

WORKDIR /python-sample
COPY pip.conf .
COPY requirements.txt .
RUN PIP_CONFIG_FILE=pip.conf pip install -r requirements.txt
COPY . /python-sample/
RUN chmod +x ./scripts/startup_server.sh
