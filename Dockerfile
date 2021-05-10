FROM python:3-slim
ADD resources/geckodriver /usr/bin/
RUN python -m pip install -U selenium
ENTRYPOINT [ "python", "src/main.py" ]
