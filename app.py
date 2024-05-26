from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/contact')
def contact():
    return "Contact us at example@example.com"

@app.route('/user/<username>')
def user_profile(username):
    return f"User Profile: {username}"

@app.route('/dashboard')
def dashboard():
    # Render an HTML template
    user = {'username': 'John Doe', 'email': 'john@example.com'}
    return render_template('dashboard.html', title='Dashboard', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
