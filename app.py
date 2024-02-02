from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>Hello, World!</h1>
    <p>My name is <strong>Flask</strong> and I am a web application framework written in Python.</p>
    <button onClick="clickMe()">Click me</button>

    <script>

        function clickMe() {
            alert('You clicked me!');
        }

    </script>
    
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)