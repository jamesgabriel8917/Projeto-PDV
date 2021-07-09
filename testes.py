import sqlite3


conn = sqlite3.connect("BancoDados.db")
c = conn.cursor()


def retornaQtd(idl):
    c.execute("""SELECT estoque FROM cadastro WHERE id=idl""".format(idl))
    result = c.fetchall()
    result = int(result[0][0])
    return result
    print('id selecionado')

print(retornaQtd(1))