from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    con = psycopg2.connect(
      database="test",
      user="test",
      password="test",
      host="db",
      port="5432"
    )

    cur = con.cursor()
    cur.execute("SELECT name from something")
    result = cur.fetchall()
    con.close()
    return("Hello " + str(result[0][0]))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
