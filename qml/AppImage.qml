import QtQuick 2.12

Item {
  id: root

  signal clicked()

  property string name: ''

  width: 50
  height: 60

  Text {
    text: root.name
  }

  Rectangle {
    anchors.fill: parent
    color: "yellow"
  }

  MouseArea {
    anchors.fill: parent
    onClicked: {
      print('mousearea clicked');
      root.clicked();
    }
  }
}
