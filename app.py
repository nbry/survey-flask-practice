from flask import Flask, request, render_template
from surveys import satisfaction_survey

app = Flask(__name__)

responses = []

@app.route('/start')
def start_page():
    import pdb
    pdb.set_trace()
    return render_template('start.html')
