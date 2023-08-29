from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        arquivo_info = instance.search(index)
        if arquivo_info.get("nome_do_arquivo") == path_file:
            print(f"Arquivo {path_file} já foi processado anteriormente.")
            return

    lines = txt_importer(path_file)

    arquivo_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(arquivo_info)

    print(arquivo_info)


def remove(instance):
    if instance.is_empty():
        return print("Não há elementos")

    index = instance.dequeue()
    return print(f"Arquivo {index['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        sys.stderr.write("Posição inválida\n")
    else:
        sys.stdout.write(str(instance.search(position)))
