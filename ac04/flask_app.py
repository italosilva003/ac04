from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

## Para rodae o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

