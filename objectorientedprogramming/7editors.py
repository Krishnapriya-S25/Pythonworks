class Editor:
    name:str
    vendor:str

    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendorc
  
    def __str__(self):
        return self.name
editor_instance1=Editor("pycham","jetbrain")

print(editor_instance1)
