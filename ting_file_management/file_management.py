import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, mode="r") as file:
            content = [line for line in file.read().split('\n')]
        return content
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
