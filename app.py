from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras
# from cryptography.fernet import Fernet
from os import environ

app = Flask(__name__)
# key=Fernet.generate_key()

host = "localhost"
port = "5432"
dbname = "crudRest"
user = "postgres" # your username
password = "sql_2023"  # your password


def get_connection():
    # funcion conexion a db
    conn = connect(host=host, port=port, dbname=dbname,
                   user=user, password=password)
    return conn

# definiendo endpoints


@app.get('/api/users')
def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    return jsonify(users)


@app.post('/api/users')
def create_users():

    new_user = request.get_json()
    username = new_user['username']
    especie = new_user['especie']
    planeta = new_user['planeta']
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('INSERT INTO users (username, especie, planeta) VALUES (%s, %s, %s) RETURNING *',
                (username, especie, planeta))
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_created_user)


@app.delete('/api/users/<id>')
def delete_users(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('DELETE FROM users WHERE id=%s RETURNING *', (id,))
    user = cur.fetchone()
    print(user)
    conn.commit()
    cur.close()
    conn.close()
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)


@app.put('/api/users/<id>')
def update_users(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    new_user = request.get_json()
    # this will be the same as before because we are using a dictionary to store our data in the
    username = new_user["username"]
    especie = new_user["especie"]
    planeta = new_user["planeta"]
    cur.execute('UPDATE users SET username = %s, especie=%s, planeta=%s WHERE id =%s RETURNING *',
                (username, especie, planeta, id))
    update_users = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if update_users is None:
        return jsonify({'message': 'user not Found'}), 404
    return jsonify(update_users)


@app.get('/api/users/<id>')
def get_user(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cur.fetchone()
    if user is None:
        return jsonify({'message': 'user not Found'}), 404
    print(user)
    return jsonify(user)

@app.get('/home')
def home():
    
    return send_file('static/templates/homePage/index.html')

@app.get('/')
def users():
    
    return send_file('static/templates/usersPage/index.html')


if __name__ == '__main__':
    app.run(debug=True)