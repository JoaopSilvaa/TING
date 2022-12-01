from ting_file_management.queue import Queue


def verify_occurrences(result):
    for i in range(0, len(result)):
        occurrences_empty = 0
        if len(result[i]["ocorrencias"]) == 0:
            occurrences_empty += 1
    return occurrences_empty


def exists_word(word: str, instance: Queue):
    result = []
    for i in range(0, len(instance)):
        data = instance.search(i)
        lines = data["linhas_do_arquivo"]
        occurrences = []
        for j in range(0, len(lines)):
            if word.lower() in lines[j].lower():
                occurrences.append({"linha": (j + 1)})
        content = {
            "palavra": word.lower(),
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": occurrences
        }
        result.append(content)

    verify = verify_occurrences(result)

    return result if verify == 0 else []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
