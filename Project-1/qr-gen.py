"""--- QR Code Generator ---"""


# pip install qrcode[pil]
# pip install pillow

# Module - qrcode
import qrcode

# Python Imaging Library - Used to handle images (Pillow)
from PIL import Image

# Version 11 represents higher version = larger QR code with more data capacity
# error_correction will adjust the error and get the QR ready to be scanned easily even if it is damaged by 30%
# ERROR_CORRECT_H - highest error correction level
# box_size represents the size of each module (box) in QR code
# border - defines the width of the border around the QR code 
qr = qrcode.QRCode(version=11, 
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=1)

# add_data adds the link of the data you want to store
qr.add_data("https://www.linkedin.com/in/vaibhavguptahere-/")

# qr.make(fit=True) adjusts the QR code size
qr.make(fit=True)

# It brings change in background and color of QR code
img = qr.make_image(fill_color="blue", back_color="black")

# It will save the QR code in the current folder where this file of code exists
img.save("web.png")
