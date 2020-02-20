import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def page(page_name='index'):
    return render_template(f'./{page_name}.html')


def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open('database.txt', 'a') as file:
        file.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as file2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(file2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@ app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou')
    else:
        return 'Not OK'
