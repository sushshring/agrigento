from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.dtmilano.android.viewclient import ViewClient

class MonkeyRunner:

    def __init__(self, apk_path, package_name, activity_name):
        self.apk_path = apk_path
        self.package_name = package_name
        self.activity_name = activity_name
        pass

    def getConnection(self):
        device, serialno = ViewClient.connectToDeviceOrExit()
        vc = ViewClient(device=device, serialno=serialno)
        self.vc = vc
        self.device = device
        pass

    def launchActivity(self, package_name=None, activity_name=None):
        if not package_name:
            package_name = self.package_name
            pass
        if not activity_name:
            activity_name = self.activity_name
            pass
        self.getConnection()
        self.device.startActivity(package_name + '/' + activity_name)
        pass

    def inputText(self, textbox, text):
        if self.vc.getSdkVersion() >= 16:
            self.vc.findViewByIdOrRaise(textbox).touch()
            self.device.type(text)
            pass
        else:
            raise TypeError("Illegal SDK version")
        pass

    def touchButton(self, button):
        if self.vc.getSdkVersion() >= 16:
            self.vc.findViewByIdOrRaise(button).touch()
            pass
        else:
            raise TypeError("Illegal SDK version")
        pass
