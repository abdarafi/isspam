FROM abdarafi/fastapi-erp:0.1
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
