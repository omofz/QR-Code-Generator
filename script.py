"""
This script generates a QR code for a given link.
If the QR code is scanned, it redirects the user to the provided link.

Usage:
    - Run interactively: python script.py
    - Run with CLI argument: python script.py "https://example.com"
"""

import sys
import qrcode
import qrcode.image.svg as img_svg

def generate_qr_code(link: str, filename="qr.svg"):
    """Generates a QR code for the given link and saves it as an SVG file."""
    img = qrcode.make(link, image_factory=img_svg.SvgImage)

    with open(filename, "wb") as qr:
        img.save(qr)

    print(f"QR code saved as {filename}")

def main():
    """Handles CLI arguments and interactive mode."""
    if len(sys.argv) > 1:  
        link = str(sys.argv[1])
    else:
        link = input("Enter the link to generate QR Code: ")

    generate_qr_code(link)

if __name__ == "__main__":
    main()
