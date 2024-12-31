from flask import Flask, jsonify
from routes import api
from db_connection import get_db_connection

# Create the Flask app
app = Flask(__name__)

app.register_blueprint(api)

# Define a simple route for testing
@app.route('/')
def home():
    return "Trail Service API is running!"














# Run the application
if __name__ == '__main__':
    app.run(debug=True)
