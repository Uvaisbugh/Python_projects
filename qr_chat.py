import qrcode
from PIL import Image

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants. ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    number = 0
    number += 1
    img.save(f"chat/code_{number}.png")
    print("QR code generated successfully")
    
def decode_qrcode(image):
    img = Image.open(image)
    result = qrcode.decode(img)
    print("Decoded text: ", result)
    
    
def main():
    option = input("Enter 1 to generate QR code or 2 to decode QR code: ")
    if option == "1":
        text = input("Enter the text to be encoded: ")
        generate_qrcode(text)
    elif option == "2":
        image = input("Enter the path to the QR code image: ")
        decode_qrcode(image)
        
if __name__ == "__main__":
    main()
    
    