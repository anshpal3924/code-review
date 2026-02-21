# Code chunking service
class ChunkingService:

    def chunk_file(self, file_path: str, text: str, chunk_size=50):
        """
        Chunk text by lines, preserving file path and line numbers.
        """
        lines = text.split("\n")
        chunks = []

        for i in range(0, len(lines), chunk_size):
            chunk_lines = lines[i:i+chunk_size]
            content = "\n".join(chunk_lines)

            chunks.append({
                "file_path": file_path,
                "content": content,
                "start_line": i + 1,
                "end_line": i + len(chunk_lines)
            })

        return chunks
