from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return '欢迎使用中文量化面板'\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000)
