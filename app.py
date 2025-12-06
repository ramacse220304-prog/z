from flask import Flask, render_template_string

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flask App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: #f0f0f0;
                }
                .container {
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 { color: #333; }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Flask! 🚀</h1>
                <p>This is a simple Flask application.</p>
                <p><a href="/about">Learn more about this app</a></p>
            </div>
        </body>
        </html>
    ''')

# About route
@app.route('/about')
def about():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>About - Flask App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: #f0f0f0;
                }
                .container {
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 { color: #333; }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>About This App</h1>
                <p>This is a simple Flask web application with two routes.</p>
                <ul>
                    <li><strong>/</strong> - Home page</li>
                    <li><strong>/about</strong> - About page</li>
                </ul>
                <p><a href="/">Go back home</a></p>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
