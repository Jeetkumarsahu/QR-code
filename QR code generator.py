import qrcode

# Step 1: Link of file (Drive or any hosting)
data = input("link of file : ")

# Step 2: QR code generation
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

# Step 3: Save as image
img = qr.make_image(fill='black', back_color='white')
img.save("file_qrcode.png")
