from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Annoh Mienza! ' 'This is my first HTML page.'

@app.route ('/hello')
def hello():
    return render_template('hello.html')
if __name__ == '__main__':
    app.run()

@app.route ('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run()


    @app.route('/teamabout')
    def about():
        return render_template('teamabout.html')


    if __name__ == '__main__':
        app.run()