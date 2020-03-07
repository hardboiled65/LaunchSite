import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Window 2.12

Window {
  id: root

  visible: true
  width: 600
  height: 400
  color: "transparent"

  Rectangle {
    anchors.fill: parent
    color: "white"
    radius: 25

    Flow {
      x: 20
      y: 20
      width: parent.width - (this.y * 2)

      // columnSpacing: 40
      spacing: 40
      Repeater {
        model: LaunchSite.appImages
        AppImage {
          name: modelData.name

          onClicked: {
            modelData.launch();
          }
        }
      }

      /*
      Rectangle {
        id: debugRect
        anchors.fill: parent
        color: "#55ff0000"
      }
      */
    }
    Rectangle {
      id: debugButton
      anchors.bottom: parent.bottom
      anchors.bottomMargin: 15
      width: 80
      height: 30
      color: "grey"
      Text {
        text: 'click'
      }
      MouseArea {
        anchors.fill: parent
        onClicked: {
          print('hello');
        }
      }
    }
  }
}
