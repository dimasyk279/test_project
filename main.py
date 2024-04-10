from flask import send_file, request, Flask
from flask import url_for, redirect, abort
from flask import  render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'GET':
        return render_template('name.html')
    else:
        name = request.form['inf1']
        surname = request.form['inf2']
        return f'{name}, {surname}'

if __name__ == '__main__':
    app.run(port=8000, debug = True)