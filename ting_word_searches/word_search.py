def exists_word(word, instance):
    results = []
    for data in instance.data:
        find_word = search_by_word(word, data["linhas_do_arquivo"])
        if find_word:
            result = {
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias":  find_word
            }
            results.append(result)
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
