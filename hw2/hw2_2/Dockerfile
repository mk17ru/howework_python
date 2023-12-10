FROM blang/latex:ctanfull

RUN apt-get update && apt-get install -y python3.9 python3-pip

RUN pip3 install -i https://pypi.anaconda.org/mk17ru/simple table-generator
RUN pip3 install pdflatex

COPY . /app

WORKDIR /app

CMD ["python3", "main.py"]
