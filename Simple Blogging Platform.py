from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (replace with a database in a real-world scenario)
posts = [
    {"id": 1, "title": "Introduction to Flask", "content": "Flask is a micro web framework for Python."},
    {"id": 2, "title": "Getting Started with Python", "content": "Python is a versatile programming language."},
    {"id": 3, "title": "Web Development Basics", "content": "Learn the basics of web development."},
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def view_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        return render_template("post.html", post=post)
    else:
        return "Post not found."

@app.route("/create", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        # Generate a unique ID for the new post
        new_post_id = max(p["id"] for p in posts) + 1

        # Create a new post
        new_post = {"id": new_post_id, "title": title, "content": content}
        posts.append(new_post)

        return redirect(url_for("home"))

    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Blog</title>
</head>
<body>
    <h1>Welcome to the Simple Blog</h1>
    <ul>
        {% for post in posts %}
            <li><a href="{{ url_for('view_post', post_id=post['id']) }}">{{ post['title'] }}</a></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('create_post') }}">Create a New Post</a>
</body>
</html>






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post['title'] }} - Simple Blog</title>
</head>
<body>
    <h1>{{ post['title'] }}</h1>
    <p>{{ post['content'] }}</p>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create a New Post - Simple Blog</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="post" action="{{ url_for('create_post') }}">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" rows="4" required></textarea>
        <br>
        <button type="submit">Create Post</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
