from flask import Flask, render_template, redirect, url_for, session, flash, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = {
            'M_test': {'password': 'M_1', 'role': 'Mentor'},
            'E_test': {'password': 'E_1', 'role': 'Employer'},
            'J_test': {'password': 'J_1', 'role': 'Jobber'}
        }

        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            if user['role'] == 'Mentor':
                return redirect(url_for('mentor_dashboard'))
            elif user['role'] == 'Employer':
                return redirect(url_for('employer_dashboard'))
            elif user['role'] == 'Jobber':
                return redirect(url_for('jobber_dashboard'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/employer/dashboard')
def employer_dashboard():
    if 'username' in session and session['role'] == 'Employer':
        return render_template('Employer/Dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/employer/job-listings')
def job_listings():
    if 'username' in session and session['role'] == 'Employer':
        return render_template('Employer/Job-Listings.html')
    else:
        return redirect(url_for('login'))

@app.route('/employer/new-job')
def new_job():
    if 'username' in session and session['role'] == 'Employer':
        return render_template('Employer/New-Job.html')
    else:
        return redirect(url_for('login'))

@app.route('/employer/candidates')
def candidates():
    if 'username' in session and session['role'] == 'Employer':
        return render_template('Employer/Candidates.html')
    else:
        return redirect(url_for('login'))

@app.route('/jobber/dashboard')
def jobber_dashboard():
    if 'username' in session and session['role'] == 'Jobber':
        return render_template('Jobber/Dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/jobber/courses')
def courses():
    if 'username' in session and session['role'] == 'Jobber':
        return render_template('Jobber/Courses.html')
    else:
        return redirect(url_for('login'))

@app.route('/jobber/hiring')
def hiring():
    if 'username' in session and session['role'] == 'Jobber':
        return render_template('Jobber/Hiring.html')
    else:
        return redirect(url_for('login'))


@app.route('/mentor/dashboard')
def mentor_dashboard():
    if 'username' in session and session['role'] == 'Mentor':
        return render_template('Mentor/Dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/mentor/courses')
def mentor_courses():
    if 'username' in session and session['role'] == 'Mentor':
        return render_template('Mentor/Courses.html')
    else:
        return redirect(url_for('login'))

@app.route('/mentor/add_courses')
def mentor_add_courses():
    if 'username' in session and session['role'] == 'Mentor':
        return render_template('Mentor/Add-Courses.html')
    else:
        return redirect(url_for('login'))

@app.route('/mentor/sales')
def mentor_sales():
    if 'username' in session and session['role'] == 'Mentor':
        return render_template('Mentor/Sales.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
