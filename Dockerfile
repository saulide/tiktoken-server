FROM python:3.10-alpine
RUN pip install flask
RUN pip install tiktoken
RUN pip install flask_cors

COPY src/tiktoken_server.py /usr/tiktoken/tiktoken_server.py
s
CMD ["python", "-m", "flask", "--app", "/usr/tiktoken/tiktoken_server.py", "run", "--host", "0.0.0.0"]

EXPOSE 5000

