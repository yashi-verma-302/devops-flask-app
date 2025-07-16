from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>DevOps Flask App</title>
        <style>
            body {
                background-color: #f0f4f8;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #333;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #007bff;
            }
            p {
                font-size: 18px;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 DevOps Flask App</h1>
            <p>Welcome! This app is running in a Docker container on your local machine.</p>
            <div class="footer">Made with 💙 using Flask + Docker</div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "UP"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>DevOps Flask App</title>
        <style>
            body {
                background-color: #f0f4f8;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #333;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #007bff;
            }
            p {
                font-size: 18px;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> DevOps Flask App</h1>
            <p>Welcome! This app is running in a Docker container on your local machine.</p>
            <div class="footer">Made with  using Flask + Docker</div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "UP"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)