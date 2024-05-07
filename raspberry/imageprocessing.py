import cv2
import numpy as np

# Funktion, um HEX von RGB zu berechnen
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Rückruffunktion für Trackbars (wird aber nicht verwendet)
def nothing(x):
    pass

# Fenster für Trackbars erstellen
cv2.namedWindow('Einstellungen', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Einstellungen', 600, 400)

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

# Funktion, um die Kamera zu überprüfen
def check_cam_device():
    if cv2.VideoCapture(1):
        print("externe kammera")
        return cv2.VideoCapture(1)
    elif cv2.VideoCapture(0):
        print("interne kammera")
        return cv2.VideoCapture(0)

# Kamera öffnen
cap = check_cam_device()

while True:
    # Bild von der Kamera einlesen
    ret, frame = cap.read()
    if not ret:
        break

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

    # Das Bild anzeigen
    cv2.imshow('Erkennung', frame)

    # Mit 'q' beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera und Fenster freigeben
cap.release()
cv2.destroyAllWindows()
