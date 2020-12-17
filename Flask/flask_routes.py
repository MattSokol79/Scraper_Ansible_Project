import pandas as pd
from flask import Flask, jsonify, redirect, url_for, render_template


# Create an instance of our app
app = Flask(__name__)

app.config['SERVER_NAME'] = (public ip of app instance)

class Import_CSV:
    def import_file(self):
        self.jobs_csv = pd.read_csv(r'C:\Users\poiro\Downloads\ItJobsWatchTop30.csv')
        self.data_frame = pd.DataFrame(self.jobs_csv, columns=['Skill / Job Role(Historical trends & salary statistics)', 'Rank6 Months to17 Dec 2020', 'RankChangeYear-on-Year', 'Median Salary6 Months to17 Dec 2020', 'Median Salary% ChangeYear-on-Year', 'HistoricalPermanentJob Ads', 'LiveJobVacancies'])
        print(self.data_frame)



# pip uninstall numpy
# pip install numpy==1.19.3