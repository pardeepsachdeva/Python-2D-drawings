class drawing:
    def createDrawing(self,name):
        self.name=name
    def displayName(self):
        print(self.name)
        return self.name


first=drawing()
second=drawing()
first.createDrawing("aa")
second.createDrawing("bb")
first.displayName()
second.displayName()
