FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install requests
RUN pip install streamlit
RUN pip install pydeck
RUN pip install pandas
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
