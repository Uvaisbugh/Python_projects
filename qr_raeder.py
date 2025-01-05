import cv2
from pyzbar import pyzbar

def decode_qr(frame):
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(points, returnPoints=True)
        else:
            hull = points
        
        n = len(hull)
        for j in range(0, n):
            cv2.line(frame, hull[j], hull[(j + 1) % n], (0, 255, 0), 3)
        
        qr_data = obj.data.decode("utf-8")
        qr_type = obj.type
        text = f"{qr_type}: {qr_data}"
        cv2.putText(frame, text, (obj.rect.left, obj.rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(f"Decoded {qr_type}: {qr_data}")
    
    return frame

def scan_qr_from_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = decode_qr(frame)
        cv2.imshow("QR Code Scanner", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def scan_qr_from_image(image_path):
    image = cv2.imread(image_path)
    frame = decode_qr(image)
    cv2.imshow("QR Code Scanner", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    choice = input("Enter 'v' for video scan or 'i' for image scan: ").strip().lower()
    if choice == 'v':
        scan_qr_from_video()
    elif choice == 'i':
        image_path = input("Enter the path to the image: ").strip()
        scan_qr_from_image(image_path)
    else:
        print("Invalid choice. Please enter 'v' or 'i'.")