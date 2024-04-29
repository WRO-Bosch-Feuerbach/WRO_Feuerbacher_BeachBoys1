// auto generated content from display configuration
import QtQuick 2.2
import QtQuick.Window 2.0
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1
import QtQuick.Extras 1.4

TXTWindow {
  Rectangle {
    id: rect
    color: "grey"
    anchors.fill: parent
  }
  TXTInput {
    id: txt_input
    text: "hello"
    onTextChanged: label1.text = txt_input.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 107
    y: 10
    width: 100
    height: 40
  }
  TXTInput {
    id: txt_input2
    text: "Farbe:"
    onTextChanged: label1.text = txt_input2.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 5
    y: 12
    width: 100
    height: 40
  }
  TXTInput {
    id: txt_input3
    text: "vorne"
    onTextChanged: label1.text = txt_input3.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 4
    y: 62
    width: 100
    height: 40
  }
  TXTInput {
    id: vorne
    text: "hello"
    onTextChanged: label1.text = vorne.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 108
    y: 62
    width: 100
    height: 40
  }
  TXTInput {
    id: rechts
    text: "hello"
    onTextChanged: label1.text = rechts.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 58
    y: 109
    width: 54
    height: 40
  }
  TXTInput {
    id: links
    text: "hello"
    onTextChanged: label1.text = links.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 170
    y: 111
    width: 49
    height: 40
  }
  TXTInput {
    id: txt_input32
    text: "rechts"
    onTextChanged: label1.text = txt_input32.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 4
    y: 109
    width: 50
    height: 40
  }
  TXTInput {
    id: txt_input33
    text: "links"
    onTextChanged: label1.text = txt_input33.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 123
    y: 107
    width: 40
    height: 40
  }
  TXTInput {
    id: hinten
    text: "hello"
    onTextChanged: label1.text = hinten.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 4
    y: 154
    width: 100
    height: 40
  }
  TXTInput {
    id: farbe
    text: "Farbe"
    onTextChanged: label1.text = farbe.text
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    horizontalAlignment: Text.AlignLeft
    color: "#444444"
    elide: Text.ElideRight
    x: 14
    y: 190
    width: 100
    height: 40
  }
  TXTCheckBox {
    id: txt_checkbox
    text: "Color Detection"
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    checked: false
    enabled: true
    x: 112
    y: 150
    width: 119
    height: 40
  }
  TXTSwitch {
    id: start
    text: "start"
    font.pixelSize: 22
    font.bold: false
    font.italic: false
    font.underline: false
    enabled: true
    checked: false
    x: 124
    y: 190
    width: 100
    height: 40
  }
}
