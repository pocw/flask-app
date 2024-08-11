
from flask import Flask, Response
import time
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def stream():
        def generate():
            while True:
                # Generate a string with 10,000 characters
                large_text = 'A' * 100000
                # Send the data to the client
                yield f"data: {large_text}\n\n"
                # Wait for 0.5 seconds
                time.sleep(1)
        return Response(generate(), mimetype='text/event-stream')

    return app
