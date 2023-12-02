def read_input(path: str) -> list:
    with open(path, "r") as f:
        return f.read().splitlines()