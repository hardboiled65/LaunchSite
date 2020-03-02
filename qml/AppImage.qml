import QtQuick 2.12

Item {
  id: root

  signal clicked()

  property string name: ''

  width: 64
  height: 64

  Rectangle {
    id: background
    anchors.fill: parent
    color: "yellow"
  }

  Image {
    id: icon
    width: 64
    height: 64
    source: '../assets/placeholder.png'
  }

  Text {
    text: root.name

    width: root.width + 60
    // width: this.implicitWidth
    elide: Text.ElideMiddle
    anchors.bottom: parent.bottom
    anchors.horizontalCenter: parent.horizontalCenter
  }

  MouseArea {
    anchors.fill: parent
    onClicked: {
      root.clicked();
    }
  }
}
