from flask import Flask, render_template, request, send_file
from main import main
from htmlTemplate import inputVariables
import time
app = Flask(__name__)
@app.route('/')
def hello_world():
    print('Creating Report...')
    return inputVariables

@app.route('/execute', methods = ['POST'])
def execute():
    startTime = time.time()
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
    print('total seconds = ' + str(endTime-startTime))
    return send_file(excel_file,
                     as_attachment=True, 
                     download_name = "WD Competitor Report.xlsx",
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    # Set the app to run on 0.0.0.0 so that it's accessible in the Heroku environment
    app.run(host='0.0.0.0', port=5000)





