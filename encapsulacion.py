class Label:
    def __init__(self,text,font): #funcion constructor
        self._text = text #set-asignar     get-obtener
        self._font = font
    def get_text(self):
        return self._text
    def set_text(self, value):
        self._text = value
    def get_font(self):
        return self._text
    def set_font(self,value):
        self._font = value 