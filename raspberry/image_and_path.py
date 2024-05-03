import cv2
import numpy as np
import json
import os

# Funktion, um HEX von RGB zu berechnen
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Rückruffunktion für Trackbars (wird aber nicht verwendet)
def nothing(x):
    pass

# JSON-Datei zum Speichern der Einstellungen
settings_file = './settings.json'

# Funktion zum Speichern der Einstellungen
def save_settings():
    settings = {
        'r_hue_min': cv2.getTrackbarPos('R Hue Min', 'Einstellungen'),
        'r_hue_max': cv2.getTrackbarPos('R Hue Max', 'Einstellungen'),
        'r_sat_min': cv2.getTrackbarPos('R Sat Min', 'Einstellungen'),
        'r_sat_max': cv2.getTrackbarPos('R Sat Max', 'Einstellungen'),
        'r_val_min': cv2.getTrackbarPos('R Val Min', 'Einstellungen'),
        'r_val_max': cv2.getTrackbarPos('R Val Max', 'Einstellungen'),
        'g_hue_min': cv2.getTrackbarPos('G Hue Min', 'Einstellungen'),
        'g_hue_max': cv2.getTrackbarPos('G Hue Max', 'Einstellungen'),
        'g_sat_min': cv2.getTrackbarPos('G Sat Min', 'Einstellungen'),
        'g_sat_max': cv2.getTrackbarPos('G Sat Max', 'Einstellungen'),
        'g_val_min': cv2.getTrackbarPos('G Val Min', 'Einstellungen'),
        'g_val_max': cv2.getTrackbarPos('G Val Max', 'Einstellungen')
    }
    with open(settings_file, 'w') as f:
        json.dump(settings, f)

# Funktion zum Laden der Einstellungen
def load_settings():
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            return json.load(f)
    else:
        return {}

# Fenster für Trackbars erstellen
cv2.namedWindow('Einstellungen', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Einstellungen', 500, 400)

# Geladene Einstellungen anwenden
settings = load_settings()

# Trackbars für die Farbschwellen
cv2.createTrackbar('B Hue Min', 'Einstellungen', settings.get('r_hue_min', 0), 179, nothing)
cv2.createTrackbar('B Hue Max', 'Einstellungen', settings.get('r_hue_max', 180), 179, nothing)
cv2.createTrackbar('B Sat Min', 'Einstellungen', settings.get('r_sat_min', 0), 255, nothing)
cv2.createTrackbar('B Sat Max', 'Einstellungen', settings.get('r_sat_max', 50), 255, nothing)
cv2.createTrackbar('B Val Min', 'Einstellungen', settings.get('r_val_min', 0), 255, nothing)
cv2.createTrackbar('B Val Max', 'Einstellungen', settings.get('r_val_max', 50), 255, nothing)

# Kamera öffnen
cap = cv2.VideoCapture(1)

while True:
    # Bild von der Kamera einlesen
    ret, frame = cap.read()
    if not ret:
        break

    # Trackbar-Werte holen
    b_hue_min = cv2.getTrackbarPos('B Hue Min', 'Einstellungen')
    b_hue_max = cv2.getTrackbarPos('B Hue Max', 'Einstellungen')
    b_sat_min = cv2.getTrackbarPos('B Sat Min', 'Einstellungen')
    b_sat_max = cv2.getTrackbarPos('B Sat Max', 'Einstellungen')
    b_val_min = cv2.getTrackbarPos('B Val Min', 'Einstellungen')
    b_val_max = cv2.getTrackbarPos('B Val Max', 'Einstellungen')

    # Bereiche für schwarz basierend auf Trackbar-Werten definieren
    black_lower = np.array([b_hue_min, b_sat_min, b_val_min])
    black_upper = np.array([b_hue_max, b_sat_max, b_val_max])

    # Bild in HSV konvertieren
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Maske für Schwarz erstellen
    black_mask = cv2.inRange(hsv, black_lower, black_upper)

    # Konturen finden
    contours, _ = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) >= 2:
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        rect1 = cv2.boundingRect(contours[0])
        rect2 = cv2.boundingRect(contours[1])

        center1 = (rect1[0] + rect1[2] // 2, rect1[1] + rect1[3] // 2)
        center2 = (rect2[0] + rect2[2] // 2, rect2[1] + rect2[3] // 2)

        midpoint = ((center1[0] + center2[0]) // 2, (center1[1] + center2[1]) // 2)

        cv2.line(frame, center1, midpoint, (255, 0, 0), 2)
        cv2.line(frame, center2, midpoint, (255, 0, 0), 2)

    # Das Bild anzeigen
    cv2.imshow('Erkennung', frame)

    # Mit 'q' beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        save_settings()
        break

# Kamera und Fenster freigeben
cap.release()
cv2.destroyAllWindows()
