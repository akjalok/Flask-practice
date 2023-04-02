## INTEGRATE HTML WITH FLASK
## HTTP ver GET and POST
##jinja 2 template
'''
{%...%} conditions,for
{{  }} expressions to print output
{#....#} for
'''
from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/pass/<int:score>')
def Pass(score):
    if score>=50:
        result = 'pass'
    else:
        result = 'fail'
    exp={'score':score,'result':result}
    return render_template('result.html',result=exp)
# @app.route('/fail/<int:score>')
# def fail(score):
#     return 'You have failed and your marks were ' + str(score)
# @app.route('/result/<int:marks>')
# def result(marks):
#     if marks>50:
#         result = 'Pass'
#     else:
#         result = 'fail'
#     return redirect(url_for(result,score=marks))
@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths  = float(request.form['maths'])
        sst = float(request.form['sst'])
        french = float(request.form['french'])
        english = float(request.form['english'])
        total_score = (maths+science+sst+french+english)/5
    return redirect(url_for('Pass',score=total_score))
if __name__ == '__main__':
    app.run(debug=True)