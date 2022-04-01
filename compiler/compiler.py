import sys





def compile_file(path: str):
    print("start compiling")
    with open(path) as file:
        for line in file:
            print(line)





if __name__ == "__main__":
    compile_file(sys.argv[1]) # python compile.py hallo.q