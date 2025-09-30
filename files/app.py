from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            port=os.environ.get('DB_PORT', 5432)
        )
        return "Database connected successfully!"
    except Exception as e:
        return f"Cannot connect to database: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
