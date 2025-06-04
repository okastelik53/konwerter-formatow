import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py input_file output_file")
    else:
        print(f"Input: {sys.argv[1]}, Output: {sys.argv[2]}")
