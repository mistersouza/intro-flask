import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as company_data:
        data = json.load(company_data)
    return render_template('about.html', page_heading='About Us', company=data)


@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as company_data:
        data = json.load(company_data)
        for obj in data:
            if 'url' in obj and obj['url'] == member_name:
                member = obj
    return render_template('member.html', dwarf=member)

@app.route('/careers')
def careers():
    return render_template('careers.html', page_heading='Careers')

if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", '0.0.0.0'),
        port=int(os.environ.get("PORT", '5000')),
        debug=True
    )