import argparse
import code

def execute_file(lines):
    for line in lines:
        code.compile_command
        print(line)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('entry_point')
    args = parser.parse_args()
    print("hello world")
    print(args.entry_point)