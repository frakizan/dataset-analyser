from analyser import Analyser
import argparse

def main():
    parser = argparse.ArgumentParser(description='YOLO Dataset Analyser')
    parser.add_argument('--dir', type=str, help='Path to the folder')
    parser.add_argument('--classes', nargs='+', type=str, help='List of classes')
    args = parser.parse_args()
    
    analyser = Analyser(args.dir, args.classes)
    
    analyser.analyse()
    
if __name__ == '__main__':
    main()