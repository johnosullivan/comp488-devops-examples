from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey y'all from Docker + Kubernetes!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # change the ports if you like