from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return 'hello world!'
@app.route('/second')
def second():
    return 'i am sony'
app.run()
