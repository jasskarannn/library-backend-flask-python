from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        dbname='dbjancuk',
        user='admin',
        password='admin'
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f'Hello, Database Version: {version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)