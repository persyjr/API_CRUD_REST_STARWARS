from flask import Flask, request, render_template, jsonify , redirect , url_for
from flask_sqlalchemy import SQLAlchemy 
#1. inicio Flask
app = Flask(__name__)

#2. configuro mi Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../dataBase/starwars.db'

#3. conexion con mi base de datos 
app.app_context().push()
db=SQLAlchemy(app)

#4. declarando mi clase Users
class Users(db.Model):
    __tablename__ = 'users' #importante definir el nombre de mi tabla en mi modelo
    id= db.Column(db.Integer, primary_key=True ) #declaro la columna id como clave primaria
    username=db.Column(db.String(200), unique=True, nullable= False)#declaro el nombre del usuario 
    especie = db.Column (db.String(200), nullable= True)
    planeta = db.Column (db.String(200), nullable= True)
    def __repr__(self):
        return f'<Users {self.username}>'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "especie": self.especie,
            "planeta": self.planeta
            # do not serialize the password, its a security breach
        }

#4.1 declarando mi clase Favoritos
class Favorites(db.Model):
    __tablename__ = 'favorites' #importante definir el nombre de mi tabla en mi modelo
    id= db.Column(db.Integer, primary_key=True ) #declaro la columna id como clave primaria
    username=db.Column(db.String, db.ForeignKey('users.username'))#traigo el user id de mi _tablename_= users
    user = db.relationship(Users)                      # relaciono la tabla de donde saco el id
    namespecie = db.Column (db.String(200), nullable= True)                
    nameplaneta = db.Column (db.String(200), nullable= True)
    namesstarship = db.Column (db.String(200), nullable= True)
    namevehicle = db.Column (db.String(200), nullable= True)
    namepeople = db.Column (db.String(200), nullable= True)
    def __repr__(self):
        return f'<Favorites {self.userId}>'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "namespecie": self.namespecie,
            "nameplaneta": self.nameplaneta
            # do not serialize the password, its a security breach
        }
"""
host = "localhost"
port = "5432"
dbname = "crudRest"
user = "postgres" # your username
password = "sql_2023"  # your password










    


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





"""
usuario=[]
@app.get('/api/users')
def get_users():
    users=Users.query.all()
    listUsers=[]
    for i in range(0,len(users)):
        (users[i].serialize())
        listUsers.append(users[i].serialize())
    
    return listUsers

@app.get('/api/users/<id>')
def get_user(id):
    user=Users.query.all()
    if user is None:
        return jsonify({'message': 'user not Found'}), 404
    print(user[id].serialize())
    return user[id].serialize()

@app.route('/api/users',methods=['POST'])
def create_users():
    new_user=Users(username=request.form['username'],especie=request.form['especie'],planeta=request.form['planeta'])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("home"))#redirecciona el metodo home 

@app.route('/api/edit/<id>')
def edit_users(id):
    usuario=Users.query.filter_by(id=int(id)).first()
    print(usuario)
    print(usuario.serialize())
    usuario=usuario.serialize()
    users=Users.query.all()
    listUsers=[]
    for i in range(0,len(users)):
        (users[i].serialize())
        listUsers.append(users[i].serialize())
    return render_template('./plantillas/usersPage/index.html', users=listUsers,usuario=usuario)

@app.route('/api/update/<id>',methods=['POST'])
def update_users(id):
    user=Users.query.filter_by(id=int(id)).first()
    user.username=request.form['username']
    user.especie=request.form['especie']
    user.planeta=request.form['planeta']
    db.session.commit()
    return redirect(url_for("home"))
@app.route('/api/delete/<id>')
def delete(id):
    user=Users.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/')
def home():
    
    users=Users.query.all()
    listUsers=[]
    for i in range(0,len(users)):
        (users[i].serialize())
        listUsers.append(users[i].serialize())
    return render_template('./plantillas/usersPage/index.html', users=listUsers)

@app.get('/home')
def homepage():
    
    return render_template('./plantillas/homePage/index.html')
if __name__ == '__main__':
    app.run(debug=True)
    