# Main script: main.py

import requests
import json
import openpyxl
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
from getJSON import getJSON as g
from PIL import Image as PILImage
from io import BytesIO

# Define the API endpoint and parameters. Domains are for finding the logo. Symbols are for finding the earnings.
domains = ['www.walkerdunlop.com','www.cbre.com','www.us.jll.com','www.wellsfargo.com','www.pnc.com']
symbols = "symbol=WD%2CCBRE%2CJLL%2CCIGI%2CWFC%2CPNC%2C"

# Excel Declarations
wb = Workbook()
ws = wb.active

# Get logo pictures
for i in range(5):
    company = g("https://brand-logo-api.p.rapidapi.com/brand/retrieve?domain=" + domains[i] ,"brand-logo-api.p.rapidapi.com")
    print(company)
    singleLogo = company['brand']['logos'][0]['url']
    print(singleLogo)

    # Paste logo into worksheet
    response = requests.get(singleLogo)
    image = PILImage.open(BytesIO(response.content))
    temp_image_path = "temp_image.png"
    image.save(temp_image_path)
    img = ExcelImage(temp_image_path)
    ws.add_image(img,"A" + str(i+2))
    wb.save('output_with_image.xlsx')


