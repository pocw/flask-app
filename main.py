from flask import Flask, jsonify
from flask import Flask, Response
import time
import os

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
            time.sleep(0.5)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
