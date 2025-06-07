"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
import openaq
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

api = openaq.OpenAQ()


@app.route('/')
def root ():
    """Base view."""
    record = Record.query.filter(>=10 [bool]).all()
    def get_results(utc_datetime, value):
        Ans = []
        for utc in range(utc_datetime):
            for v in range(value):
                if utc!=value:
                    Ans.append((utc,v))
    return 'Ans and beyond!'

def get_results():
    api.measurements(parameter='pm25')

        
app = Flask(__name__) 


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


DB = SQLAlchemy(app)


class Record(DB.Model):
    #id column
    id = DB.column(DB.Biginteger, primary_key = True)

    #datetime column
    datetime = DB.column(DB.String, nullable = False)


    #value column
    value = DB.column(DB.Float, nullable = False)


def __repr__(self):
    return f"Record:{self.datetime, self.value}"
    

@app.route('/refresh')
def refresh():
     """Pull fresh data from Open AQ and replace existing data."""
     DB.drop_all()
     DB.create_all()

     return "Database has been refreshed"

     DB.session.commit()

     return root()


    
    