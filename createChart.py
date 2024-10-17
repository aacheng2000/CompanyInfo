import xlsxwriter
import pandas as pd
import openpyxl
from openpyxl import Workbook

def createChart(worksheetName, workbook, dates, values):
    # Create a new Excel file and add a worksheet
    #workbook = xlsxwriter.Workbook('area_chart_example.xlsx')
    worksheet = workbook(worksheetName)

    # Example data: a range of dates and corresponding values
    #dates = pd.date_range(start='2024-01-01', periods=10, freq='D').strftime('%Y-%m-%d').tolist()
    #values = [10, 20, 15, 25, 30, 28, 33, 35, 40, 38]

    # Write the date and value data to the worksheet
    worksheet.write('A1', 'Date')  # Column header for dates
    worksheet.write('B1', 'Value')  # Column header for values
    worksheet.write_column('A2', dates)  # Write dates in column A
    worksheet.write_column('B2', values)  # Write values in column B

    # Create an area chart object
    chart = workbook.add_chart({'type': 'line'})

    # Configure the series with data from the worksheet
    chart.add_series({
    'categories': '=Sheet1!$A$2:$A$11',  # Dates for the x-axis
    'values': '=Sheet1!$B$2:$B$11',      # Values for the y-axis
    'name': 'Values',
    })

    # Add chart title and axis labels
    chart.set_title({'name': 'Date vs Value'})
    chart.set_x_axis({'name': 'Date'})
    chart.set_y_axis({'name': 'Value'})

    # Insert the chart into the worksheet
    worksheet.insert_chart('D2', chart)

    # Close the workbook
    workbook.close()

    print("Excel file created with an area chart.")
