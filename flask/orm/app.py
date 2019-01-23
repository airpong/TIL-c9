from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#sqlAlchemy 초기화
db=SQLAlchemy(app)
# migrate 초기화
migrate = Migrate(app, db)
#table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
    
#명령어
#flask db migrate
#flask db upgrade
#flask db init

#정리
#Create
#INSERT INTO users (username,email) VALUES ('airpong','giponge@gmail.com')
#user = User(username='airpong',email='giponge@gmail.com')
#db.session.add(user)
#db.session.commit()

# [Read]
# SELECT * FROM users;
# users = User.query.all() # 복수

# SELECT * FROM users WHERE username='airpong';
# users = User.query.filter_by(username='airpong').all()

# SELECT * FROM users WHERE username='airpong' LIMIT 1;
# users = User.query.filter_by(username='airpong').first()

# SELECT * FROM users WHERE id=2 LIMIT 1; => id = primarykey
# users = User.query.get(2)
# primary key만 get으로 가져올 수 있음.

#SELECT * FROM users Like email LIKE '%water%'
#users = User.query.filter(User.email.like("%example%")).all()

#ORDER
#users = User.query.order_by(User.username).all()

#LIMIT
#users = User.query.limit(1).all()

#OFFSET
# users = User.query.offset(2).all()

#Order + Limit + OFFSET
#users = User.query.order_by(User.username).limit(1).offset(2).all()