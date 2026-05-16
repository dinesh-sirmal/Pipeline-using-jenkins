from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps CI/CD Project</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }

            .container {
                margin-top: 120px;
                padding: 40px;
            }

            h1 {
                font-size: 45px;
                margin-bottom: 10px;
            }

            p {
                font-size: 20px;
                color: #e0e0e0;
            }

            .card {
                margin: 30px auto;
                padding: 20px;
                width: 60%;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
                backdrop-filter: blur(5px);
            }

            .btn {
                margin-top: 20px;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                background-color: #00c6ff;
                color: white;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
            }

            .btn:hover {
                background-color: #0072ff;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 DevOps CI/CD Pipeline</h1>
            <p>Automated Deployment using Jenkins + Docker</p>

            <div class="card">
                <h2>Project Status</h2>
                <p>✔ Flask App Running</p>
                <p>✔ Docker Container Active</p>
                <p>✔ Jenkins CI/CD Working</p>

                <button class="btn" onclick="alert('Pipeline is working successfully!')">
                    Check Pipeline Complete
                </button>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)