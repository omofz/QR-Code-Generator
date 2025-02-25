# QR Code Generator

This script generates a QR code for a given link. Once scanned, the QR code redirects the user to the provided URL. The QR code is saved as an SVG image.

## Features
- Generates QR codes from user-provided URLs.
- Saves QR codes in **SVG** format.
- Can be used **interactively** or via **command-line arguments**.

## Prerequisites
Make sure you have Python installed on your system. You also need the `qrcode` library.

### Install dependencies:
```sh
pip install qrcode[pil]
```

## Usage

### Run Interactively
If no link is provided as an argument, the script will prompt the user for a URL:
```sh
python script.py
```
Then, enter the link manually when prompted.

### Run with Command-Line Argument
You can also provide the URL directly as a command-line argument:
```sh
python script.py "https://example.com"
```
This will generate a QR code for `https://example.com` and save it as `qr.svg`.

## Example Code
```python
import sys
import qrcode
import qrcode.image.svg as img_svg

def generate_qr_code(link: str, filename="qr.svg"):
    img = qrcode.make(link, image_factory=img_svg.SvgImage)
    with open(filename, "wb") as qr:
        img.save(qr)
    print(f"QR code saved as {filename}")

def main():
    if len(sys.argv) > 1:
        link = str(sys.argv[1])
    else:
        link = input("Enter the link to generate QR Code: ")
    generate_qr_code(link)

if __name__ == "__main__":
    main()
```

## Output
The generated QR code will be saved as `qr.svg` in the same directory as the script.

## License
This project is open-source and available under the MIT License.

