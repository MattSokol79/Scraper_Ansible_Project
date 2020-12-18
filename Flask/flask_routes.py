import pandas as pd
from flask import Flask, jsonify, redirect, url_for, render_template


# Create an instance of our app
app = Flask(__name__)

# Server name is the public ip of the live environment
app.config['SERVER_NAME'] = 'localhost:3000'


    # pip uninstall numpy
    # pip install numpy==1.19.3

@app.route('/')
def homepage():
    jobs_csv = pd.read_csv(r"C:\Users\poiro\Downloads\ItJobsWatchTop30.csv", encoding='unicode_escape')


    return render_template("webpage.html", name='ITJobsWatch Top 30', data=jobs_csv.to_html())


if __name__ == "__main__":
    app.run(debug=True)
