# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

def func(filename):
    lista = []
    maxcol = 0

    with open(filename, 'r') as f:
        for line in f:
            file_content = line
            file_content = str(file_content[:-1]).split(",")

            lista.append(file_content)
            if len(file_content) > maxcol:
                maxcol = len(file_content)

    return lista, maxcol
