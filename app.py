import datetime
from flask import Flask, render_template, jsonify, request, url_for, redirect

app = Flask(__name__)


class StrJsConvertor:
    def __init__(self, valueStr):
        self.valueStr = valueStr
        self.LastUpdate = datetime.datetime.now()
        #self.valueJson = ""


@app.route('/api/StrJsonConvertor', methods = ['POST','GET'])
def StrJsonConvertor():
    param1 = request.args.get('param')
    # Create a JSON response
    response = {'message': f'Value entered: {param1}'}
    return jsonify(response)


@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            #get the i/p param from req Query String
            entered_value = request.form['content']
            input_Content = StrJsConvertor(valueStr = entered_value)
            # Convert to Json
            response = {'message': f'Paramter Entered:{input_Content.valueStr}'}
            input_Content.valueJson = jsonify(response).response[0]
            #print(Sjc.valueJson)
            return render_template('index.html', input_Content = input_Content)
            #return 'hello'
        except:
            return 'There was an Error Converting String to Json'
    else:
        return render_template('index.html')
    


if __name__ == "__main__":
    app.run(debug=True)
    