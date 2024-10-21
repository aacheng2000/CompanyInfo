from flask import Flask, render_template, request, send_file
from main import main
from htmlTemplate import inputVariables
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Creating Report...')
    return inputVariables






'<form action="/execute" method="POST"><input type="text" id="stock1" name="stock1"><br><br><input type="text" id="stock2" name="stock2"><br><br><input type="text" id="stock3" name="stock3"><br><br><input type="text" id="stock4" name="stock4"><br><br><input type="text" id="stock5" name="stock5"><br><br><input type="text" id="stock6" name="stock6"><br><br><button type="submit">Run Python Function</button></form>'
  #  return '<form action="/execute" method="POST"><button type="submit">Run Python Function</button></form>'
    
## 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max


@app.route('/execute', methods = ['POST'])
def execute():
    startTime = time.time()
    #print(startTime)
    stock1 = request.form.get('stock1')
    stock2 = request.form.get('stock2')
    stock3 = request.form.get('stock3')
    stock4 = request.form.get('stock4')
    stock5 = request.form.get('stock5')
    stock6 = request.form.get('stock6')
    timePeriod = request.form.get('timePeriod')
    excel_file = main(stock1,stock2,stock3,stock4,stock5,stock6, timePeriod)
    endTime = time.time()
    params = request.args.to_dict()
    print(request.form.get('stock1'))
    #print (endTime)
    print('total seconds = ' + str(endTime-startTime))
    return send_file(excel_file,
                     as_attachment=True, 
                     download_name = "WD Competitor Report.xlsx",
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    # Set the app to run on 0.0.0.0 so that it's accessible in the Heroku environment
    app.run(host='0.0.0.0', port=5000)
    print("hello there __name if!")




