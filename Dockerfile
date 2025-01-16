FROM python

WORKDIR /code

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt --index-url https://pypi.org/simple

COPY . .



