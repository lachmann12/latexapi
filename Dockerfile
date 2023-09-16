FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /latex

#RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get -y install \
    python3-pip \
	vim \
	wget \
	gcc \
	musl-dev \
    g++ \
    texlive-base \
    texlive-latex-extra \
    imagemagick
	

WORKDIR /latex

COPY requirements.txt /latex
RUN pip3 install -r requirements.txt

RUN sed -i '/disable ghostscript format types/,+6d' /etc/ImageMagick-6/policy.xml

COPY main.py /latex
ADD static /latex/static

EXPOSE 5050

ENTRYPOINT ["uvicorn", "main:app", "--port", "5557", "--host", "0.0.0.0"]
