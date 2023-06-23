import os
from .bounding_box import BoundingBox

class Label():
    def __init__(self, name:str) -> None:
        self.name = name
        self.bboxes = []


    def read_data(self) -> list:
        # if the file doesn't exists, it must be created
        # try:    
        #     with open(self.name, 'x') as f:
        #         f.close()
        # except:
        #     pass

        with open(self.name, 'r') as f:
            for line in f.readlines():
                line = line.strip().split(' ')
                bbox = BoundingBox(line[0], float(line[1]), float(line[2]), float(line[3]), float(line[4]))
                self.bboxes.append(bbox)
                f.close()

        return self.bboxes
