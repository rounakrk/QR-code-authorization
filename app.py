from flask import Flask, render_template, request, redirect, url_for
from login_and_registration import login_web, signup_web
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/employee/<name>')
def emp_log(name):
    return "Hello "+name

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/new_employee/<name>')
def new_emp_log(name):
    return "Hello new employee "+name

@app.route('/login')
def new_login():
    return render_template('index.html')

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        result = request.form
        # return redirect(url_for('emp_log', name = result['username']))
        list1 = [result['username'], result['password']]
        print(list1)
        ret = login_web(list1)
        if ret:
            return render_template('idCard.html', name = [ret[0],ret[1]+'.png'] )
        else:
            return "Wrong Credentials"
        # return render_template('idCard.html', name = ['Rounak', 'Agarwal'] )


@app.route('/new_employee', methods=['GET', 'POST'])
def new_employee():
    if request.method == 'POST':
        result = request.form
        if result['password'] == result['conf_password']:
            ret = signup_web([result['username'], result['email'], result['password']])
            if ret:
                return "Your profile is created now go to login"
            else:
                return "Some error"
        # return redirect(url_for('new_emp_log', name = result['username']))
        else:
            return "Passwords are not same."

@app.route('/empid')
def empid():
    return render_template('idCard.html')

#For selecting the QR image from the static folder
@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='images/' + filename), code=301)


if __name__ == '__main__':
    app.run(debug=True)