import cv2
import numpy as np

def count_tickets():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale and blur to remove noise
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Thresholding: Isolate white objects (adjust 200 based on your room lighting)
        _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

        # Find contours (the outlines of the white shapes)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        ticket_count = 0
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            # Filter by area to ignore tiny white specks
            if area > 1500:  
                x, y, w, h = cv2.boundingRect(cnt)
                
                # Optional: Filter by aspect ratio if your "tickets" are a specific shape
                # aspect_ratio = float(w)/h
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                ticket_count += 1

        # Display the count on the screen
        cv2.putText(frame, f"Live Kitchen Rush: {ticket_count} Tickets", (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Show the video feed
        cv2.imshow("KitchenSync - Live Monitor", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    count_tickets()