import ep3
import sys, os

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_name = ep3.convert_text(f'[Converted]{os.path.basename(input_path)}')
    ep3.process(input_path, output_name)

if __name__ == '__main__':
    main()