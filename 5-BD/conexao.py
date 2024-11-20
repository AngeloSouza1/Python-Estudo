import psycopg2

conn = psycopg2.connect(
database="fliperama",
user="angelo_souza",
password="1234",
host="localhost",
port= '5432'
)
