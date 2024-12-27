import tkinter as tk
from tkinter import messagebox

def generate_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save("qrcode.png")
    
class QrGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")
        self.geometry("400x150")

        self.url_label = tk.Label(self, text="Enter URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack()

        self.generate_button = tk.Button(self, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

    def generate_qr_code(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return

        generate_qrcode(url)
        messagebox.showinfo("Success", "QR code generated successfully")

if __name__ == '__main__':
    app = QrGeneratorApp()
    app.mainloop()