import pandas as pd
from flask import Flask, jsonify, redirect, url_for, render_template


# Create an instance of our app
app = Flask(__name__)

# Server name is the public ip of the live environment
app.config['SERVER_NAME'] = '34.244.153.28'

class Import_CSV:
    def import_file(self):
        self.jobs_csv = pd.read_csv(r'C:\Users\poiro\Downloads\ItJobsWatchTop30.csv')
        self.data_frame = pd.DataFrame(self.jobs_csv, columns=['Skill / Job Role(Historical trends & salary statistics)', 'Rank6 Months to17 Dec 2020', 'RankChangeYear-on-Year', 'Median Salary6 Months to17 Dec 2020', 'Median Salary% ChangeYear-on-Year', 'HistoricalPermanentJob Ads', 'LiveJobVacancies'])
        print(self.data_frame)
        # pip uninstall numpy
        # pip install numpy==1.19.3

@app.route('/')
def home():
    return render_template("webpage.html")


if __name__ == "__main__":
    app.run(debug=True)
