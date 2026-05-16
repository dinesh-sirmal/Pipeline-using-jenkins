from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>DevOps CI/CD Demo Project</h1>
    <p>If you change code and push to GitHub, Jenkins redeploys automatically.</p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
