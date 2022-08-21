from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user='root', passwd='password')
cursor = mydb.cursor()


@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="password", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__ == '__main__':
    app.run()