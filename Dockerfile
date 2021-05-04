FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir /app/
COPY ./ /app/
WORKDIR /app
COPY ./pip.conf /root/.pip/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./main.py"]




