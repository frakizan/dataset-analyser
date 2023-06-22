class BoundingBox():
    def __init__(self, _class:str, xc:float, yc:float, w:float, h:float):
        self._class = _class
        self.xc = xc
        self.yc = yc
        self.w = w
        self.h = h