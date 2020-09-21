from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, url_for, redirect, render_template

app = Flask(__name__)

dbuser = 'postgres'
password = 'essa'
netloc = 'localhost'
port = 5432
dbname = 'rest_test'

DB_URL = f'postgresql://{dbuser}:{password}@{netloc}:{port}/{dbname}'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning

db = SQLAlchemy(app)


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['POST'])
def add_user():
    user = User(request.form['i_text'])
    db.session.add(user)
    db.session.commit()
    return redirect('/')


@app.route('/delete')
def delete():
    #User.query.delete(synchronize_session=False)
    q = db.session.query(User)
    q.delete()
    db.session.commit()
    return redirect('/')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<User: {self.name}>'


#if __name__ == '__main__':
    #app.run()
