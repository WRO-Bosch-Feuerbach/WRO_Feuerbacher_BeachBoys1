# Documentation of Team 1, Bosch Feuerbach
---

## Members und deren Rollen:
|Name|Rolle|
|-|-|
|Robin Kaiser (PEA6-Fe-Fi)|Entwicklung und Bau|
|Jonathan Zimmer (PEA6-Fe-Fi)|Entwicklung|
|Erik Reichelt (PEA2-Fe-EGS2)|Bau|

## Teile und deren Funktion
| Teil Name | Funktion |
| -         | -        |
| Ultraschall-Sensor | Abstand zwischen Wand/Hindenissen und dem Roboter messen |
| Servo | Lenkung |
| Encoder Motor | Antrieb der Hinterachse (mit Differentialgetriebe) |
| TXT 4.0 Controller | STeuerung des Roboters |
| Batterie (8,4v) | Stromversorgung des Roboters und seiner Bestandteile |

Weitere Information zu genauer Funktion und Integration [hier](#energie--sensoren) und [hier](#motorisierung)

### Motorisierung
Die Motorisierung des Roboters besteht aus zwei Bestandteilen:
1. Encoder Motor (Fischertechnik)

### Energie & Sensoren
Für die Stromversorgung wird ein 8,4V 1800mAh Fischertechnik Akku verwendet. Es werden insgesamt 6 Ultraschallsensoren und eine Kamera verwendet. Die Ultraschallsensoren messen die Abstände zur nächsten Wand, mit der Kamera soll eine Farberkennung durchgeführt werden.

### Hindernisse
Die Farbe der Hindernisse wird von der Kamera erkannt und ausgewertet, dementsprechend lenkt der Roboter ein. Die Ultraschallsensoren überprüfen parallel ob der Roboter dem Hinderniss zu nah kommt.