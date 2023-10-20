from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/thankyou/<name>')
def thank_you(name):
	return render_template('thankyou.html', name=name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		name = data['name']
		email = data['email']
		subject = data['subject']
		msg = data['message']
		file = database.write(f'\n{name},{email},{subject},{msg}')
		database.close()

def write_to_csv(data):
	with open('database.csv',newline='', mode='a') as database2:
		name = data['name']
		email = data['email']
		subject = data['subject']
		msg = data['message']
		csv_writer = csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,msg])
		database2.close()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect(url_for('thank_you', name=data['name']))
		except:
			return 'did not save to database'
	else:
		'something went wrong. Try again!'