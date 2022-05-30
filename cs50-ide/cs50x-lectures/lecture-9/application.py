from flask import Flask, render_template, request

app = Flask(__name__)

# Python decorator - apply one function to another
@app.route('/', methods=['GET', 'POST'])
def index(): # Doesn't need to specify the directory to the file
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        return render_template('greet.html', name=request.form.get('first_name', 'world'))
