from flask import*
app=Flask(__name__)
@app.route('/')
def greet():
    return render_template('hello.html')
if __name__=='__main__':
    app.run()
