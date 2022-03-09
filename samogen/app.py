import flask


app = flask()

@app.route('/')
def home():
    return('index.html')




if name == 'main':
    app.run()
