import argparse

from .analyser import Analyser

def main():
    parser = argparse.ArgumentParser(description='YOLO Dataset Analyser')
    parser.add_argument('--dir', help='Path to the folder', required=True)
    parser.add_argument('--classes', nargs='+', type=str, help='List of classes')
    args = parser.parse_args()
    
    analyser = Analyser(args.dir, args.classes)
    
    analyser.analyse()
    
if __name__ == '__main__':
    main()
