import qrcode

# Ask user for input
data = input("Enter URL or text to generate QR Code: ")

# Ask user for file name
file_name = input("Enter file name to save QR Code (without .png): ")

# Create QR code object with settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save(f"{file_name}.png")

print("✅ QR Code generated successfully! 🎉")
