# QR Code Generator

This Python script generates a QR code for a given URL or any other text input. The QR code is saved as an image file in the specified location.

## Features
- Generates a QR code from any text or URL.
- Saves the QR code as a PNG image.
- Customizable QR code size, colors, and error correction level.

## Requirements
- Python 3.6 or higher
- `qrcode` library

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install the required library:
   ```bash
   pip install "qrcode[pil]"
   ```

## Usage
1. Copy the script below and save it as `generate_qr.py`:
   ```python
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
   ```

2. Replace `https://your-website-link.com` with the desired URL or text to encode.
3. Run the script:
   ```bash
   python generate_qr.py
   ```

4. The QR code will be saved as `qrcode.png` in the same directory as the script.

## Customization
### Change QR Code Colors
Modify the `fill_color` and `back_color` in the `qr.make_image` method to customize the colors:
```python
qr_image = qr.make_image(fill_color="blue", back_color="yellow")
```

### Save to a Specific Location
Provide a full file path to the `save` method:
```python
qr_image.save("C:/Users/YourName/Desktop/qrcode.png")
```

### Adjust QR Code Size
Change the `version` parameter to control the size of the QR code:
- `version=1`: Smallest size
- `version=40`: Largest size

### Error Correction Levels
- `qrcode.constants.ERROR_CORRECT_L`: About 7% error recovery
- `qrcode.constants.ERROR_CORRECT_M`: About 15% error recovery (default)
- `qrcode.constants.ERROR_CORRECT_Q`: About 25% error recovery
- `qrcode.constants.ERROR_CORRECT_H`: About 30% error recovery

## Output
The script generates a QR code image named `qrcode.png` in the current working directory.

## Example
Here is an example of a generated QR code:

![QR Code Example](https://via.placeholder.com/150)

## License
This script is open-source and free to use under the MIT License.

