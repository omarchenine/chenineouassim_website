from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='/Users/omar/Documents/web_html:css /portfolio-website/.env')


app = Flask(__name__)

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # For Gmail
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Your email (use environment variable for security)
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Your email password (use environment variable for security)
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  # Default sender address

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Simple validation
        if not name or not email or not message:
            return "Please fill out all fields.", 400

        # Send email using Flask-Mail
        try:
            msg = Message(
                subject="New Message from Portfolio Contact Form",
                recipients=["sifoomar7@gmail.com"],
                body=f"Message from {name} ({email}):\n\n{message}"
            )
            mail.send(msg)
            return redirect(url_for('thankyou'))  # Redirect to thank you page or message
        except Exception as e:
            # Log the error or take action
            return f"Error: {str(e)}", 500

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')  # You can create a thankyou.html template to display a custom thank you message

if __name__ == '__main__':
    app.run(debug=True)