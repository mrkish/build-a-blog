from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(5000))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_title = request.form['blog']
        new_blog =Blog(blog_title)
        db.session.add(new_blog)
        db.session.commit()

    blogs = Blog.query.all()
    completed_blogs = Blog.query.all()
    return render_template('blog.html', title="Blogs!", blogs=blogs)

@app.route('/newpost', methods=['POST','GET'])
def newpost():

    

    return render_template('newpost.html',title='New Post')


#@app.route('/delete-blog', methods=['POST'])
#def delete_blog():
#
#    blog_id = int(request.form['blog-id'])
#    blog = blog.query.get(blog_id)
#    return redirect('/')
#    blog.completed = True
#    db.session.add(blog)
#    db.session.commit()


if __name__ == '__main__':
    app.run()
