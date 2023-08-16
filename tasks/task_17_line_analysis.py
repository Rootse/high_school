def LineAnalysis(line: str) -> bool:
    if not line.startswith('*') or not line.endswith('*'):
        return False

    pattern = line[1:-1].split('*')
    pattern_len = len(pattern[0])

    return all(len(p) == pattern_len for p in pattern)
