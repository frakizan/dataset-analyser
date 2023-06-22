from pathlib import Path
from label import Label

class Analyser():
    def __init__(self, folder_path:str, classes:list) -> None:
        self.folder_path = folder_path
        self.statistics = {str(key): 0 for key in classes}
        self.statistics['total'] = 0
    
    def analyse(self) -> None:
        path = Path(self.folder_path)

        for img_path in path.rglob('*'):
            if img_path.is_file() and img_path.suffix.lower() in ('.png', '.jpg'):
                label_path = string_path = img_path.as_posix()[0:-3:1] + 'txt'
                label = Label(label_path)
                self.analyse_label(label)
        
        for _class in self.statistics.keys():
            if _class != 'total':
                try:
                    print(self.statistics)
                    print(f"{_class} : {round((self.statistics[_class]/self.statistics['total']) * 100)}%")
                except:
                    print("error: the dataset is empty")

    def analyse_label(self, label:Label) -> None:
        for bbox in label.read_data():
            self.statistics['total'] += 1
            if bbox._class in list(self.statistics.keys()):
                self.statistics[bbox._class] +=1
            
        

