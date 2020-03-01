import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Window 2.12

Window {
  id: root

  visible: true
  width: 600
  height: 400
  color: "black"

  Rectangle {
    anchors.fill: parent
    color: "white"
    radius: 25

    GridLayout {
      x: 20
      y: 20

      columnSpacing: 40
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
  }
}
