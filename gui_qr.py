import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qrcode(url):
    """Generates a QR code image for the given URL and saves it as qrcode.png."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    return img

class QrGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")
        self.geometry("500x300")
        self.resizable(False, False)

        # URL Input Section
        self.url_label = tk.Label(self, text="Enter URL:", font=("Arial", 12))
        self.url_label.pack(pady=5)

        self.url_entry = tk.Entry(self, width=60, font=("Arial", 12))
        self.url_entry.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(self, text="Generate QR Code", font=("Arial", 12),
                                         command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        # QR Code Display Section
        self.qr_label = tk.Label(self)
        self.qr_label.pack(pady=10)

    def generate_qr_code(self):
        """Generates and displays the QR code."""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return

        try:
            qr_image = generate_qrcode(url)
            # Convert to a format that Tkinter can display
            qr_tk_image = ImageTk.PhotoImage(qr_image)

            # Update the label to display the QR code
            self.qr_label.configure(image=qr_tk_image)
            self.qr_label.image = qr_tk_image

            messagebox.showinfo("Success", "QR code generated successfully! It has been saved as 'qrcode.png'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == '__main__':
    app = QrGeneratorApp()
    app.mainloop()
