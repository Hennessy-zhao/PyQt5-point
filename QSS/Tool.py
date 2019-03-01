class QSSTool:

    #静态方法
    @staticmethod
    def setQssToObj(file_path,obj):

        with open(file_path, "r") as f:
            content = f.read()
            obj.setStyleSheet(content)
