from abc import ABC,abstractmethod
class Editor(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def write(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod    
    def execute(self):
        pass


class VsCode(Editor):
    def open(self):
        print("Vscde open method")
    

    def write(self):
        print("Vscde write method")
    
        
    def debug(self):
        print("Vscde debug method")
    
       

    def execute(self):
         print("Vscde execute method")

vscode_instance=VsCode()
vscode_instance.open()
    
        