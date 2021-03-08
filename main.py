from flask import Flask, request, render_template
from mytool import *
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    robozin = GetIps(text)
    return render_template('index.html', all_vpc=robozin.get_all_vpc(),
                           all_npc=robozin.get_all_npc(),
                           ip_100_mb=robozin.get_ip_100mb(),
                           ip_250_mb=robozin.get_ip_250mb(),
                           ip_500_mb=robozin.get_ip_500mb(),
                           ip_1gb=robozin.get_ip_1gb(),
                           ip_relatorio=robozin.get_relatorio())


if __name__ == '__main__':
    app.run(debug=True, use_debugger=True, use_reloader=False)
