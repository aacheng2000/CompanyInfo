inputVariables = '''<form action="/execute" method="POST">
  Please enter up to six stock symbols
  <br /><br /><input 
    type="text" 
    id="stock1" 
    name="stock1" 
    value="WD" />
  <br /><br /><input 
    type="text" 
    id="stock2" 
    name="stock2"
    value = "CBRE" />
  <br /><br /><input
    type="text"
    id="stock3"
    name="stock3"
    value = "JLL" />
  <br /><br /><input
    type="text"
    id="stock4"
    name="stock4"
    value = "MMI"
  />
  <br /><br /><input
    type="text"
    id="stock5"
    name="stock5"
    value = "NMRK"
  />
  <br /><br /><input
    type="text"
    id="stock6"
    name="stock6"
    value = "LADR"
  /><br><br>

Time Period
<br><br>
    <label for="timePeriod">Choose a time period below. Note: it may take 15 seconds for report to complete.</label>
    <select id="timePeriod" name="timePeriod" value = "5d">
        <option value="1d">1 day</option>
        <option value="5d">5 days</option>
        <option value="1mo" selected>1 month</option>
        <option value="6mo">6 months</option>
        <option value="1y">1 year</option>
        <option value="5y">5 years</option>
        <option value="10y">10 years</option>
        <option value="ytd">years to date</option>
        <option value="max">max</option>
    </select>





  <br /><br /><button type="submit">Generate Report</button>
</form>'''