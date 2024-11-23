from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

posts = [
    {"id": 1, "title": "First Blog Post", "content": "Welcome to my personal blog!", "author": "Alyssa Brewer"},
    {"id": 2, "title": "Another Post", "content": "Flask makes creating blogs easy!", "author": "Alyssa Brewer"}
]

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post is None:
        return "Post not found!", 404
    return render_template('post.html', post=post)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {"id": len(posts) + 1, "title": title, "content": content, "author": "Alyssa Brewer"}
        posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('add_post.html')


if __name__ == '__main__':
    app.run(debug=True)
