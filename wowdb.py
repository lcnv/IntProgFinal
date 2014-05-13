from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.Text, primary_key = True)
    login = db.Column(db.String)
    server = 

# class Enrollment(db.Model):
#     __table__ = 'enrollment'
#     course_num = db.Column(db.Integer, db.ForeignKey('course.course_num'))
#     student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))



enrollment = db.Table('post_tag',
    db.Column('tag_id',db.Integer, db.ForeignKey('tag.tag_id')),
    db.Column('post_id',db.Integer, db.ForeignKey('post.post_id')),
    db.Column('tag_date',db.DateTime)
)

class Post(db.Model):
    __tablename__ = 'post'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    text = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=post_tag,
                                backref=db.backref('posts',lazy='dynamic'))

class Tag(db.Model):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    first_date = db.Column(db.DateTime)
    desc = db.Column(db.Text)

db.drop_all()
db.create_all()

p1 = Post(post_id=1, title='first post',author='Guy Dude', text='hibbly jibbly woot de doo')
p2 = Post(post_id=1, title='second post',author='Some Guy', text='hibbly jibbly woot de doot doo')
db.session.add_all([p1,p2])

t1 = Tag(tag_id=1, name='silly', first_date=datetime.datetime.now() , desc='The post is kind of silly')

#s1 = Student(student_id=1,first_name='Brad',last_name='Miller')
#s2 = Student(student_id=2,first_name='Jane',last_name='Miller')
#s3 = Student(student_id=3,first_name='Josh',last_name='Miller')
#db.session.add_all([s1,s2,s3])
#c1 = Course(course_num=150,building='Olin',room='202',students=[s1,s2])
#c2 = Course(course_num=365,building='Olin',room='202')
#db.session.add(c1)
#db.session.add(c2)

#s4 = Student(student_id=4,first_name='John',last_name='Doe',courses=[c1,c2])
#db.session.add(s4)

db.session.commit()
