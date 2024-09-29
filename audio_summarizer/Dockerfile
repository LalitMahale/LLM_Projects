From python:3.10

WORKDIR /application

COPY requirements.txt .

# install requirements.
RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000


CMD [ "streamlit" , "run","Summerization.py" ]