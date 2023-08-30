def exists_word(word, instance):
    lista = list()

    for indice in range(len(instance)):
        ocorrencia = list()
        for index, linha in enumerate(
                instance.search(indice)["linhas_do_arquivo"], start=1):
            if word.lower() in linha.lower():
                ocorrencia.append({"linha": index})
        if ocorrencia:
            resultado = {
                "palavra": word,
                "arquivo": instance.search(indice)["nome_do_arquivo"],
                "ocorrencias": ocorrencia
                }
            lista.append(resultado)
    return lista


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
