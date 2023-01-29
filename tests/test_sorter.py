from testing.sort_2 import FileSystem, FileWordsSorter

### Attempt 1

def _test_file_words_sorter__sort_words():
    """
    First attempt at writing a test before implementation.

    Does not test behavior. 
    """
    sorter = Sorter()
    sorted_words = sorter.sort(words=["abc", "aaz"])
    assert sorted_words == ["aaz", "abc"]


### Attempt 2

class FakeFileSystem(FileSystem):
    def __init__(self) -> None:
        self.file_contents: dict[str, str] = {}

    def load(self, filepath: str) -> str:
        return self.file_contents[filepath]

    def write(self, filepath: str, content: str) -> None:
        self.file_contents[filepath] = content

def test_file_words_sorter__sort_words():
    """
    Given an input file and an output file,
    should load the input file, sort the words and write to the output file.
    """
    fake_file_system = FakeFileSystem()
    fake_file_system.write("input.txt", "ac,ab")

    file_words_sorter = FileWordsSorter(fake_file_system)
    file_words_sorter.sort("input.txt", "output.txt")

    assert fake_file_system.load("output.txt") == "ab,ac"

