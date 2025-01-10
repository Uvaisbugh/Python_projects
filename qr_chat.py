import os
import qrcode
import cv2

class QRCodeApp:
    def __init__(self):
        self.output_dir = "chat"
        self.ensure_output_directory()

    def ensure_output_directory(self):
        """Ensure the output directory exists."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_qrcode(self, text):
        """Generate a QR code from the given text."""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="white", back_color="black")

        # Save the QR code image with a unique filename
        number = len(os.listdir(self.output_dir)) + 1
        img.save(os.path.join(self.output_dir, f"code_{number}.png"))
        print(f"QR code generated successfully: {self.output_dir}/code_{number}.png")


    def decode_qrcode(image_path):
        """Decode the QR code from the given image using OpenCV."""
        try:
            img = cv2.imread(image_path)
            detector = cv2.QRCodeDetector()
            data, bbox, _ = detector(img)

            if data:
                print("Decoded text:", data)
            else:
                print("No QR code found in the image.")
        except Exception as e:
            print(f"Error decoding QR code: {e}")

    def run(self):
        """Run the main application loop."""
        while True:
            option = input("Enter 1 to generate QR code or 2 to decode QR code (or 'exit' to quit): ")
            if option == "1":
                text = input("Enter the text to be encoded: ")
                self.generate_qrcode(text)
            elif option == "2":
                image_path = input("Enter the path to the QR code image: ")
                self.decode_qrcode(image_path)
            elif option.lower() == 'exit':
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = QRCodeApp()
    app.run()