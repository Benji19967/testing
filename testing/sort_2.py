from abc import ABC, abstractmethod


class FileSystem(ABC):
    """
    Abstraction of the real file handling.

    This allows us to test everything (except the implementation of this abstraction)
    quickly and efficiently, in memory.

    Should be as simple and generic as possible to limit chances
    that this abstraction will introduce a bug.

    Should be simpler than the technology that it wraps (our code is only
    using a subset of all functionality).

    Integration tests should then take care of asserting that the real implementation
    of this abstraction is bug free.
    """

    @abstractmethod
    def load(self, filepath: str) -> str:
        pass

    @abstractmethod
    def write(self, filepath: str, content: str) -> None:
        pass

class FileWordsSorter:
    
    SEPARATOR = ","

    def __init__(self, file_system: FileSystem) -> None:
        self.file_system = file_system

    def sort(self, input_file: str, output_file: str) -> None:
        input_file_content = self.file_system.load(input_file)

        words = input_file_content.split(self.SEPARATOR)
        words.sort()

        self.file_system.write(output_file, f"{self.SEPARATOR}".join(words))