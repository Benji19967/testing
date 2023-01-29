from abc import ABC, abstractmethod


class FileSystem(ABC):
    """
    Abstraction of the real file handling.
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