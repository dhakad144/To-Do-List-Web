from flask import Flask, render_template, request, session
import numpy as np
from doads import *


app = Flask(__name__)
app.secret_key = 'your_secret_key'  
obj = DOADS('data.csv')  


@app.route('/')
def index():
    """"root function """
    new = np.array(obj.df).tolist()
    return render_template('index.html',data = new)


@app.route('/editsumit', methods=['POST'])
def editsumit():
    """edit sumit function """
    task_id = request.form.get('id')
    description = request.form.get('textarea_description')
    status = request.form.get('input_status')

    if status == 'on':  
        obj.tickcomplete(task_id)
    else: 
        obj.untickcomplete(task_id)

    obj.updatedescrip(task_id, description)

    new = np.array(obj.df).tolist()
    return render_template('index.html',data = new)


@app.route('/addsumit', methods=['POST'])
def addsumit():
    """add function """

    description = request.form.get('A_textarea_description')
    obj.appendrow(description)

    new = np.array(obj.df).tolist()
    return render_template('index.html',data = new)


if __name__ == '__main__':
    app.run(debug=True)
