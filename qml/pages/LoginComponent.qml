import QtQuick 2.0
import Sailfish.Silica 1.0
import io.thp.pyotherside 1.3
import harbour.sailfish_sinaweibo.sunrain 1.0

Page {
    id:loginComponent
    property string api_key:"211160679"
    property string api_secret:"1e6e33db08f9192306c4afa0a61ad56c"
    property string redirect_uri:"http://oauth.weico.cc"
    signal loginSucceed()
    signal loginFailed(string fail)
    SilicaFlickable {
        anchors.fill: parent

        BusyIndicator {
            id:busyIndicator
            parent: loginComponent
            anchors.centerIn: parent
            size: BusyIndicatorSize.Large
        }

        Column {
            id:column
            anchors{
                top:parent.top
                topMargin: Theme.paddingLarge*4
                horizontalCenter: parent.horizontalCenter
            }

            spacing: Theme.paddingMedium

            PageHeader {
                title: qsTr("Login")
            }

            Rectangle {
                id:rectangle
                width: input.width + Theme.paddingMedium*2
                height: input.height + Theme.paddingMedium*2
                border.color:Theme.highlightColor
                color:"#00000000"
                radius: 30
                Column {
                    id:input
                    anchors{
                        top:rectangle.top
                        topMargin: Theme.paddingMedium
                    }

                    spacing: Theme.paddingMedium

                    TextField {
                        id:userName
                        width:loginComponent.width - Theme.paddingLarge*4
                        height:implicitHeight
                        inputMethodHints:Qt.ImhNoAutoUppercase | Qt.ImhUrlCharactersOnly
                        font.pixelSize: Theme.fontSizeMedium
                        placeholderText: qsTr("Enter Email")
                        label: qsTr("UserName")
                        EnterKey.enabled: text || inputMethodComposing
                        EnterKey.iconSource: "image://theme/icon-m-enter-next"
                        EnterKey.onClicked: password.focus = true
                    }
                    TextField {
                        id:password
                        width:loginComponent.width - Theme.paddingLarge*4
                        height:implicitHeight
                        echoMode: TextInput.Password
                        font.pixelSize: Theme.fontSizeMedium
                        placeholderText: qsTr("Enter Password")
                        label: qsTr("Password")
                        EnterKey.iconSource: "image://theme/icon-m-enter-next"
                        EnterKey.onClicked: {
                            submitButton.focus = true
                            errorLabel.visible = false;
                            busyIndicator.running = true;
                            py.login(API_KEY,API_SECRET,REDIRECT_URI,userName.text,password.text)
                        }
                    }
                }
            }
            Button {
                id:submitButton
                anchors.horizontalCenter: parent.horizontalCenter
                text: qsTr("Login")
                onClicked: {
                    errorLabel.visible = false;
                    busyIndicator.running = true;
                    py.login(api_key,api_secret,redirect_uri,userName.text,password.text)

                }
            }

        }

        Label {
            id:errorLabel
            anchors{
                top:column.bottom
                topMargin: Theme.paddingLarge * 2
                bottom: parent.bottom
                bottomMargin: Theme.paddingLarge
                horizontalCenter: parent.horizontalCenter
            }
            width: column.width
            color: Theme.highlightColor
            wrapMode: Text.WrapAtWordBoundaryOrAnywhere
            font.pixelSize: Theme.fontSizeExtraSmall
        }
    }

    Python{
        id:py
        signal pyhandler(string access_token,string uid)

        onPyhandler:{
          //登录成功
          if("Error" != access_token){
            errorLabel.visible = false;
            busyIndicator.running = false;
            loginComponent.loginSucceed();
            tokenProvide.token = access_token;
            tokenProvide.uid = uid;
          }else{
            busyIndicator.running = false;
            errorLabel.visible = true;
            //uid暂时用来返回错误信息吧
            errorLabel.text = qsTr("Login fail")+" [ "+uid+" ]. " + qsTr("Please try again.");
          }

        }
        onError: {
          busyIndicator.running = false;
          errorLabel.visible = true;
          errorLabel.text = traceback;
        }
        Component.onCompleted: {
            addImportPath(Qt.resolvedUrl('../py'));
            py.importModule('main', function () {
            });
            setHandler('pyhandler', pyhandler);
        }
        function login(api_key,api_secret,redirect_uri,username,password){
            call('main.login',[api_key,api_secret,redirect_uri,username,password],function(result){
                //return result
            })
        }
    }
}
