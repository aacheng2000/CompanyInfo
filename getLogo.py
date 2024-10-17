import openpyxl
from openpyxl.drawing.image import Image
import requests
from PIL import Image as PILImage
from io import BytesIO

# Function to download the image from the URL
def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        img_data = BytesIO(response.content)
        return PILImage.open(img_data)
    else:
        print("Error: Could not download the image.")
        return None

# Save the downloaded image to a file
def save_image_to_file(image, file_name):
    image.save(file_name)

# Create an Excel file and insert the image
def insert_image_to_excel(image_file, excel_file, sheet_name='Sheet1'):
    # Open or create the Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name

    # Insert the image into Excel
    img = Image(image_file)
    sheet.add_image(img, 'A1')  # 'A1' is the cell where the image will be placed

    # Save the Excel workbook
    workbook.save(excel_file)

#def test(imageUrl, ))
# URL of the image you want to insert
image_url = 'https://example.com/image.jpg'

image_url = 'https://logo.clearbit.com/marcusmillichap.com'

# Download and save the image
#image = download_image(image_url)
#if image:
#    image_file_name = 'downloaded_image.png'  # Save as PNG or JPG
#    save_image_to_file(image, image_file_name)

    # Insert the image into Excel
#    excel_file_name = 'output.xlsx'
#    insert_image_to_excel(image_file_name, excel_file_name)

#    print(f"Image has been inserted into {excel_file_name} successfully.")