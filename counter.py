from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
