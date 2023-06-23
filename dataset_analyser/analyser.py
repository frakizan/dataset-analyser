from pathlib import Path

from .label import Label

class Analyser():
    def __init__(self, folder_path:str, classes:list) -> None:
        self.folder_path = folder_path
        self.statistics = {str(key): 0 for key in classes}
        self.statistics['total'] = 0
    
    def analyse(self) -> None:
        path = Path(self.folder_path)

        for label_path in path.rglob('*'):
            if img_path.is_file() and img_path.suffix.lower() == '.txt':
                label = Label(label_path)
                self.analyse_label(label)
        
        print(self.statistics)

    def analyse_label(self, label:Label) -> None:
        for bbox in label.read_data():
            self.statistics['total'] += 1
            if bbox._class not in list(self.statistics.keys()):
                self.statistics[bbox._class] = 1
            else:
                self.statistics[bbox._class] += 1
            
        

