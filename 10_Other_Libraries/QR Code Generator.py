import qrcode

# Generate qrcode
data = input("Enter your data to generate QR Code you want: ")

# Generate and save QR Code.
img = qrcode.make(data)
img.save("simple_qr.png")

print("Your QR Code generated successfully!")
