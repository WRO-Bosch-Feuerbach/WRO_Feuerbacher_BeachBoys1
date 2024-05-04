import cv2
import numpy as np
import time

# Funktion, um HEX von RGB zu berechnen
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Rückruffunktion für Trackbars (wird aber nicht verwendet)
def nothing(x):
    pass

# Fenster für Trackbars erstellen
cv2.namedWindow('Einstellungen')

# Trackbars für Rotbereich
cv2.createTrackbar('R Hue Min', 'Einstellungen', 0, 179, nothing)
cv2.createTrackbar('R Hue Max', 'Einstellungen', 10, 179, nothing)
cv2.createTrackbar('R Sat Min', 'Einstellungen', 100, 255, nothing)
cv2.createTrackbar('R Sat Max', 'Einstellungen', 255, 255, nothing)
cv2.createTrackbar('R Val Min', 'Einstellungen', 70, 255, nothing)
cv2.createTrackbar('R Val Max', 'Einstellungen', 255, 255, nothing)

# Trackbars für Grünbereich
cv2.createTrackbar('G Hue Min', 'Einstellungen', 35, 179, nothing)
cv2.createTrackbar('G Hue Max', 'Einstellungen', 85, 179, nothing)
cv2.createTrackbar('G Sat Min', 'Einstellungen', 100, 255, nothing)
cv2.createTrackbar('G Sat Max', 'Einstellungen', 255, 255, nothing)
cv2.createTrackbar('G Val Min', 'Einstellungen', 100, 255, nothing)
cv2.createTrackbar('G Val Max', 'Einstellungen', 255, 255, nothing)

# Kamera öffnen
cap = cv2.VideoCapture(0)

# Zeitpunkte für Timer für grüne und rote Erkennung
green_timer, red_timer = 0, 0

while True:
    # Bild von der Kamera einlesen
    ret, frame = cap.read()
    if not ret:
        break

    # Bildgröße und Mittellinie berechnen
    height, width = frame.shape[:2]
    mid_x = width // 2

    # Aktuelle Trackbar-Werte für Rot holen
    r_hue_min = cv2.getTrackbarPos('R Hue Min', 'Einstellungen')
    r_hue_max = cv2.getTrackbarPos('R Hue Max', 'Einstellungen')
    r_sat_min = cv2.getTrackbarPos('R Sat Min', 'Einstellungen')
    r_sat_max = cv2.getTrackbarPos('R Sat Max', 'Einstellungen')
    r_val_min = cv2.getTrackbarPos('R Val Min', 'Einstellungen')
    r_val_max = cv2.getTrackbarPos('R Val Max', 'Einstellungen')

    # Aktuelle Trackbar-Werte für Grün holen
    g_hue_min = cv2.getTrackbarPos('G Hue Min', 'Einstellungen')
    g_hue_max = cv2.getTrackbarPos('G Hue Max', 'Einstellungen')
    g_sat_min = cv2.getTrackbarPos('G Sat Min', 'Einstellungen')
    g_sat_max = cv2.getTrackbarPos('G Sat Max', 'Einstellungen')
    g_val_min = cv2.getTrackbarPos('G Val Min', 'Einstellungen')
    g_val_max = cv2.getTrackbarPos('G Val Max', 'Einstellungen')

    # Bereiche für rote und grüne Farbe basierend auf Trackbar-Werten definieren
    red_lower = np.array([r_hue_min, r_sat_min, r_val_min])
    red_upper = np.array([r_hue_max, r_sat_max, r_val_max])
    green_lower = np.array([g_hue_min, g_sat_min, g_val_min])
    green_upper = np.array([g_hue_max, g_sat_max, g_val_max])

    # Bild in HSV konvertieren
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Maske für Rot und Grün erstellen
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)

    # Konturen finden
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Rote Konturen in Gelb einrahmen
    for cnt in contours_red:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

            # Durchschnittliche Farbe im Bereich berechnen
            roi = frame[y:y+h, x:x+w]
            avg_color_per_row = np.average(roi, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0).astype(int)
            avg_hex = rgb_to_hex(avg_color)

            # Text schreiben
            text = f'RGB: {avg_color}, HEX: {avg_hex}'
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # rot --> rechts, wenn Kontur links von Mittellinie ist
            if x < mid_x:
                if time.time() - red_timer > 0.5:
                    print("rot --> rechts")
                    red_timer = time.time()

    # Grüne Konturen in Gelb einrahmen
    for cnt in contours_green:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

            # Durchschnittliche Farbe im Bereich berechnen
            roi = frame[y:y+h, x:x+w]
            avg_color_per_row = np.average(roi, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0).astype(int)
            avg_hex = rgb_to_hex(avg_color)

            # Text schreiben
            text = f'RGB: {avg_color}, HEX: {avg_hex}'
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # grün --> links, wenn Kontur rechts von Mittellinie ist
            if x + w > mid_x:
                if time.time() - green_timer > 0.5:
                    print("grün --> links")
                    green_timer = time.time()

# Kamera und Fenster freigeben
cap.release()
