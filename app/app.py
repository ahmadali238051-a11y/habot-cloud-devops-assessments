API_KEY = "sk_test_1234567890abcdef"
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Habot Cloud DevOps Assessment"}


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(debug=True)