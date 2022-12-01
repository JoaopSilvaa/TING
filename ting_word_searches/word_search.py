from ting_file_management.queue import Queue


def verify_occurrences(result):
    for i in range(0, len(result)):
        occurrences_empty = 0
        if len(result[i]["ocorrencias"]) == 0:
            occurrences_empty += 1
    return occurrences_empty


def iterator_in_instance_with_content(word, data):
    lines = data["linhas_do_arquivo"]
    occurrences = []
    for j in range(0, len(lines)):
        if word.lower() in lines[j].lower():
            occurrences.append({"linha": (j + 1), "conteudo": lines[j]})
    return occurrences


def iterator_in_instance_without_content(word, data):
    lines = data["linhas_do_arquivo"]
    occurrences = []
    for j in range(0, len(lines)):
        if word.lower() in lines[j].lower():
            occurrences.append({"linha": (j + 1)})
    return occurrences


def verify_generics(word, instance, type_verify):
    result = []
    for i in range(0, len(instance)):
        data = instance.search(i)
        occurrences = type_verify(word, data)
        content = {
            "palavra": word.lower(),
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": occurrences
        }
        result.append(content)

    verify = verify_occurrences(result)

    return result if verify == 0 else []


def exists_word(word: str, instance: Queue):
    return verify_generics(
        word,
        instance,
        iterator_in_instance_without_content)


def search_by_word(word, instance):
    return verify_generics(
        word,
        instance,
        iterator_in_instance_with_content)
