import QtQuick 2.12

Item {
  id: root

  signal clicked()

  property string name: ''

  width: 50
  height: 60

  Rectangle {
    anchors.fill: parent
    color: "yellow"
  }

  Text {
    text: root.name
    anchors.bottom: parent.bottom
    anchors.horizontalCenter: parent.horizontalCenter
  }

  MouseArea {
    anchors.fill: parent
    onClicked: {
      print('mousearea clicked');
      root.clicked();
    }
  }
}