# Simple Blogging Platform

This project is a Simple Blogging Platform implemented in Python using Flask. The platform allows users to view a list of blog posts, view individual posts, and create new posts.

## How It Works

1. **Flask Setup:**
    - The `app.py` script initializes a Flask web application.
2. **Routes:**
    - The `/` route (`home` function) displays a list of blog posts.
    - The `/post/<int:post_id>` route (`view_post` function) displays a specific blog post.
    - The `/create` route (`create_post` function) allows users to create a new blog post.
3. **Sample Data:**
    - `posts` is a list containing sample blog post data (replace with a database in a real-world scenario).
4. **HTML Templates:**
    - `index.html` displays a list of blog posts with links to view each post.
    - `post.html` displays the content of a specific blog post.
    - `create.html` provides a form to create a new blog post.
5. **Create Post Function:**
    - The `create_post` function handles both GET and POST requests.
    - For GET requests, it renders the `create.html` template.
    - For POST requests, it retrieves form data, generates a unique ID for the new post, creates the post, and redirects to the home page.

## Usage

1. **Run the Script:**
    - Save the script in a file, for example, `app.py`.
    - Run the script using a Python interpreter:
        
        ```bash
        python app.py
        
        ```
        
    - Open a web browser and go to http://127.0.0.1:5000/ to view the Simple Blogging Platform.
2. **Customization:**
    - Replace the sample data with a database for real-world use.
    - Add more features such as user authentication, comments, and categories.
    - Customize the HTML templates and styles for a better user interface.
    - Deploy the application to a web hosting platform for public access.

Feel free to explore and modify this project based on your specific requirements and preferences!

---

## Author

Jeel patel
