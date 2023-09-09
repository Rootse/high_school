import os


def file_search(path: str, depth: int) -> list[str]:
    if depth == 0:
        return []

    files = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            files += file_search(file_path, depth - 1)
        else:
            files.append(file_path)
    return files
