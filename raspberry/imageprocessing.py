import cv2
import numpy as np

# Bereich für rote Farbe in HSV
red_lower = np.array([0, 100, 100])
red_upper = np.array([10, 255, 255])

# Bereich für grüne Farbe in HSV
green_lower = np.array([40, 40, 40])
green_upper = np.array([70, 255, 255])

# Kamera öffnen
cap = cv2.VideoCapture(0)

while True:
    # Bild von der Kamera einlesen
    ret, frame = cap.read()
    if not ret:
        break

    # Bild in HSV konvertieren
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Maske für Rot und Grün erstellen
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)

    # Überprüfen, ob rote oder grüne Objekte gefunden werden
    red_detected = cv2.countNonZero(red_mask) > 0
    green_detected = cv2.countNonZero(green_mask) > 0

    if red_detected:
        cv2.putText(frame, "Rotes Objekt erkannt", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    elif green_detected:
        cv2.putText(frame, "Grünes Objekt erkannt", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Das Bild anzeigen
    cv2.imshow('Erkennung', frame)

    # Mit 'q' beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera und Fenster freigeben
cap.release()
cv2.destroyAllWindows()