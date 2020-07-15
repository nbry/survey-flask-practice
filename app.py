from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'springboardsurveyapp'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def root_page():
    surv_title = satisfaction_survey.title
    surv_instruct = satisfaction_survey.instructions
    return render_template('root.html', title=surv_title, instructions=surv_instruct)

@app.route('/starting', methods=["POST"])
def start_survey():
    session['responses'] = []
    return redirect('/questions/1')

@app.route('/questions')
def redirect_home():    
    return redirect ('/')

@app.route('/questions/<int:quest_num>')
def question(quest_num):
    try:
        session['responses']
    except:
        return redirect ('/')
    if len(session['responses']) >= len(satisfaction_survey.questions):
        return redirect('/thank-you')
    if len(session['responses']) + 1 != quest_num:
        flash('Please follow the questions in order', 'error')
        return redirect(f'/questions/{len(session["responses"]) + 1}')

    surv_question = satisfaction_survey.questions[quest_num - 1].question
    surv_choices = satisfaction_survey.questions[quest_num - 1].choices

    return render_template('question.html', question=surv_question, choices=surv_choices, quest_num=quest_num)


@app.route('/answers', methods=["POST"])
def answer():
    try:
        request.form["form-answer"]
    except:
        flash('please choose an answer', 'error')
        return redirect(f'/questions/{len(session["responses"]) + 1}')
        
    surv_questions = satisfaction_survey.questions
    answer = request.form["form-answer"]
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses
    
    if len(session['responses']) >= len(surv_questions):
        return redirect('/thank-you')
    else:
        next_q = len(session['responses']) + 1
        return redirect(f'questions/{next_q}')


@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

