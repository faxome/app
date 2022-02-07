from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import calendar, urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Date, default=datetime.today().date())


def __repr__(self):
    return '<Quotes>' % self.id


def get_data(url):
    xml_data = urllib.request.urlopen(url)
    xml_page_content = xml_data.read()
    soup = BeautifulSoup(xml_page_content, 'xml')
    metal_name = ['Aurum', 'Argentum', 'Platinum', 'Palladium']
    try:
        for tag in soup.findAll('Record'):
            price = tag.find("Buy").text
            date_obj = datetime.strptime(tag["Date"], '%d.%m.%Y')
            get_code = tag["Code"]
            quotes = Quotes(price=price, date=date_obj, name=metal_name[int(get_code)-1])
            db.session.add(quotes)
            db.session.commit()
        return print('ok, data getting')
    except:
        return print('error')
    else:
        render_template("index.html")


def get_url():
    today = datetime.today()
    month_days = calendar.monthrange(today.year, today.month)
    url = f'https://www.cbr.ru/scripts/xml_metall.asp?date_req1=01/0{today.month}/{today.year}&date_req2={month_days[1]}/0{today.month}/{today.year}'
    return url


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/about')
def about():

    return render_template("about.html")


@app.route('/quotes')
def view():
    today = datetime.now()
    data_list = Quotes.query.order_by(Quotes.date).all()
    return render_template("quotes.html", data_list=data_list, today=today)


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    data_list = Quotes.query.order_by(Quotes.date).all()
    if data_list == []:
        data_list.append('id')
    else:
        print("The data has already been uploaded")

    if request.method == "POST":
        try:
            db.drop_all()
            db.create_all()
            xml_url = get_url()
            get_data(xml_url)
            return redirect('/')
        except:
            return print('... something went wrong')
    else:
            return render_template("dashboard.html", data_list=data_list)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
