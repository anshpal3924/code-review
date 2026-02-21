class CodeChunk:
    def __init__(self, file_path: str, content: str, start_line: int, end_line: int):
        self.file_path = file_path
        self.content = content
        self.start_line = start_line
        self.end_line = end_line
