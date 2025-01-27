from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def greet():
    # Return a greeting message
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    # Set the host and port for the app
    app.run(host='0.0.0.0', port=5000)

