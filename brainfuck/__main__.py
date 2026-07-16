import sys
from .interpreter import interpret


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.bf>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    if not filename.endswith(".bf"):
        raise ValueError("Error: Expected a .bf file")

    with open(filename, "r") as f:

        program = f.read()
        interpret(program)


if __name__ == "__main__":
    main()

