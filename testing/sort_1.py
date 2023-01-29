# Quick and dirty way to solve the problem
# Hard to test -- pretty much have to manually run the script with real files.

IN_FILE_PATH = "in_words.txt"
OUT_FILE_PATH = "out_words.txt"

if __name__ == "__main__":
    with open(IN_FILE_PATH) as f:
        words = list(f.readlines())

    sorted_words = sorted(words)

    with open(OUT_FILE_PATH) as f:
        f.writelines(words)
