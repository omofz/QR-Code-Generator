# QR Code Generator

A simple QR code generator written in Python using the `qrcode` library. This script takes a user's link as input and generates a QR code, storing it as an image file.

## Features
- Generates QR codes from user-provided URLs
- Saves QR codes in image format (JPG, PNG, etc.)
- Simple and easy to use

## Prerequisites
Make sure you have Python installed on your system. You also need to install the `qrcode` and `Pillow` libraries.

```sh
pip install qrcode[pil]
```

## Usage
1. Clone the repository or download the script.
2. Run the script and enter the URL when prompted.
3. The QR code will be generated and saved as an image file.

### Example Code
```python
import qrcode

def generate_qr_code(link, filename="qrcode.jpg"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    user_link = input("Enter the link to generate QR Code: ")
    generate_qr_code(user_link)
```

## Output
The generated QR code will be saved as `qrcode.jpg` in the same directory as the script.

## License
This project is open-source and available under the MIT License.

