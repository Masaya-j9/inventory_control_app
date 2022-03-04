FROM python:3.7

WORKDIR /app
ENV FLASK_APP=api
ENV FLASK_ENV=development

COPY /requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]