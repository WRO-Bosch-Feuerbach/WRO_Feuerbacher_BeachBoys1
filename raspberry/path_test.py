import cv2
import numpy as np

# Funktion zur Erkennung der schwarzen Wände
def detect_walls(image):
    # Konvertiere das Bild in den HSV-Farbraum
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Definiere den unteren und oberen Schwellenwert für schwarze Farbe in HSV
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 30])

    # Erzeuge eine Maske, die nur schwarze Bereiche des Bildes enthält
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Finde Konturen der schwarzen Bereiche
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Zeichne die Konturen auf das Originalbild
    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    return image

# Hauptfunktion
def main():
    # Webcam öffnen
    cap = cv2.VideoCapture(1)

    while True:
        # Bild von der Webcam erfassen
        ret, frame = cap.read()
        if not ret:
            break

        # Wände erkennen
        detected_image = detect_walls(frame)

        # Bild anzeigen
        cv2.imshow('Detected Walls', detected_image)

        # Auf 'q' drücken, um das Programm zu beenden
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Webcam freigeben und alle Fenster schließen
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
