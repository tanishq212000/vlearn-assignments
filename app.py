#sample python hello world app
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

#additional code to test the app
import requests

def test_app():
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200
    assert 'Hello, World!' in response.text

# Run the test
if __name__ == '__main__':
    test_app()
    print("Test passed!")

