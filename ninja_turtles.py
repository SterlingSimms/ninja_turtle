from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('/index.html')
@app.route('/ninja')
def ninja():
    return render_template('/ninja.html')
@app.route('/ninja/red')
def red():
    return render_template('red.html')
@app.route('/ninja/blue')
def blue():
    return render_template('blue.html')
@app.route('/ninja/purple')
def purple():
    return render_template('purple.html')
@app.route('/ninja/orange')
def orange():
    return render_template('orange.html')
@app.route('/ninja/<vararg>')
def other(vararg):
    return render_template('other.html')
app.run(debug=True)
