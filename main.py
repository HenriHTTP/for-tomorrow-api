from  flask  import Flask 

app = Flask(__name__)


@app.route('/index')
def GetIndex (): 
    return "page index"


if __name__ == '__main__':
     app.run(debug=True)