from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/selection/')
def selection():
    return render_template('selection.html')

if __name__ == '__main__':
    app.run(debug=True)
