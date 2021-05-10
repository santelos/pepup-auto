FROM python:3-slim
RUN python -m pip install -U selenium
RUN cp geckodriver /usr/bin/
ENTRYPOINT [ "python", "main.py" ]