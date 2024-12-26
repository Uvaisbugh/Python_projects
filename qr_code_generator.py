import qrcode

def generate_qr_code(data, filename):
    img = qrcode.make(data)
    img.save(filename)

if __name__ == '__main__':
    data = input("Enter the data for the QR code: ")
    filename = input("Enter the filename for the QR code: ")
    generate_qr_code(data, filename)
