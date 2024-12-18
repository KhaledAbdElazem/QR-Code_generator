import qrcode

# Data to encode
data = "https://your-website-link.com"  # Replace with your website URL

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is smallest, 40 is largest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create the QR code image
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_image.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")
