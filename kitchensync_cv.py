import cv2
import numpy as np

def count_tickets():
    
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        ticket_count = 0
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1500:  
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                ticket_count += 1

        cv2.putText(frame, f"Live Kitchen Rush: {ticket_count} Tickets", (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        cv2.imshow("KitchenSync - Live Monitor", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    count_tickets()
