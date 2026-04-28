import qrcode
data = """Hi, my name is Yashi Srivastava,This is my first QR code project"""
img = qrcode.make(data)
img.save("my_qr.png")
print("QR Code Generated!")