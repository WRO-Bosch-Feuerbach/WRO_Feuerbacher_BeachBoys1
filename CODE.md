# Code
### Our Code is split into two parts:
- #### Code for the Fischertechnik-Controller: [Click here](./dev/)
- #### Code for the Raspberry Pi: [Click here](./raspberry/)
---

### Fischertechnik Code:
The Code for the Fischertechnik-Controller is for steering, driving, and pathfinding via the Sensors. You can find all the used Parts [here](./DOCUMENTATION.md#table-of-contents).

#### Development:
The Code was developed via a Blockly-Code-Generator used for the "Coding" and uploading on the Fischertechnik Controller. This Program is called "[ROBO Pro Coding](https://apps.microsoft.com/detail/9mxpk52r734c?hl=de-de&gl=DE)" and is a In-House Fischertechnik Product. It also is the only IDE usable to program, connect to and upload programms to the Fischertechnik Controller itselve.

#### hier doku von fischertechnik

### Logik
Der Roboter überprüft dauernd die Abstände zu den Wänden, wenn der Abstand vorne einen bestimmten Abstand unterschreitet prüft er ob der Abstand rechts oder links größer ist und lenkt dann dementsprechend in die Richtung mit mehr Platz. Wenn Der Abstand vorne so klein wird, dass der Roboter nicht mehr am Hinderniss vorbei kommt, fährt er erst rückwärts und lenkt dann nochmal ein.