import qrcode

img = qrcode.make("https://youtube.com/@trickstergamer_1?si=eCa2-5LyPEp3L2YI")
img.save("web_qr.png")