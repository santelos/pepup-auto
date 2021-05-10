FROM python:3-slim
RUN python -m pip install -U selenium
RUN cp resources/geckodriver /usr/bin/
ENTRYPOINT [ "python", "src/main.py" ]