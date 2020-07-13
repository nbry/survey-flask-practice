from flask import Flask, request, render_template
from surveys import satisfaction_survey

app = Flask(__name__)

responses = []

@app.route('/')
def root_page():
    surv_title = satisfaction_survey.title
    surv_instruct = satisfaction_survey.instructions
    return render_template('root.html', title=surv_title, instructions=surv_instruct)


@app.route('/questions/<int:quest_num>')
def question(quest_num):
    surv_question = satisfaction_survey.questions[quest_num -1].question
    surv_choices  = satisfaction_survey.questions[quest_num -1].choices
    return render_template('question.html', question=surv_question, choices=surv_choices, quest_num=quest_num)