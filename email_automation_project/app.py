from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Make sure your HTML file is named index.html

@app.route('/send-email', methods=['POST'])
def send_email():
    recipients = request.form['recipients']
    subject = request.form['subject']
    email_content = request.form['email_content']
    frequency = request.form['frequency']

    # Here you can process the data and save it to a CSV file
    data = {
        'Recipients': [recipients],
        'Subject': [subject],
        'Content': [email_content],
        'Frequency': [frequency]
    }

    # Convert to DataFrame and append to CSV
    df = pd.DataFrame(data)
    df.to_csv('emails.csv', mode='a', header=False, index=False)

    return "Email automation created successfully!"

if __name__ == '__main__':
    app.run(debug=True)