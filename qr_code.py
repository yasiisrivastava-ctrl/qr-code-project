import qrcode
data = "https://yasiisrivastava-ctrl.github.io/qr-code-project/"
img = qrcode.make(data)
img.save("my_qr.png")
