import sys
from queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    content = txt_importer(path_file)
    file_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }

    already_exist = 0
    for i in range(0, len(instance)):
        if (instance
                .search(i)["nome_do_arquivo"] == (
                    file_process["nome_do_arquivo"])):
            already_exist += 1

    if already_exist == 0:
        instance.enqueue(file_process)
        print(file_process, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
