"""
Creado por Vinicio Valbuena
Esto es un programa guia para la tarea colocada a mis hermanos.

Reglas:
    - No se utilizara ninguna función con excepción de lower, len, print, int, range.
    - Como base de datos solo se utilizara un array de una dimensión (Array 1D).
    - La base de datos debe iniciar con algun dato de referencia.
    - La base de datos debe poder grabar nuevos datos.
    - (Opcional) se puede guardar/cargar la base de datos en disco.
    - Todos los datos se harán tipados, esto no aporta nada,
    pero hará mas sencillo de leer el codigo.
    - Se permite la creación de funciones y clases, en este ejemplo no se harán
    uso de ellas.
    - IMPORATANTE: PROGRAMAR EN INGLES.
"""

"""
Base de datos
# -> describe un usuario.
@ -> puede describir un correo o el indice a dicho correo.
"""
agenda : [str] = [
        "#vinicio @2",
        "#lowlevel @2",
        "@lowlevel.1989@gmail.com",
        "#vicky @4",
        "@vicky@gmail.com",
]

HELP_INFO : str = \
"""
HELP:
    > help
        ...
    > list
        vinicio
        vicky
    > info vinicio
        lowlevel.1989@gmail.com
    > new
    name > luis
    mail > luis@gmail.com
    > exit
"""

# Comandos soportados
COMMAND_EXIT = ["exit", "quit", "e", "q"]
COMMAND_HELP = ["help", "h", "?"]
COMMAND_LIST = ["list", "l", "all", "a"]
COMMAND_NEW  = ["new",  "n"]
COMMAND_INFO = ["info", "show", "i", "s"]
COMMAND_SUPPORT = COMMAND_EXIT + COMMAND_LIST + COMMAND_NEW + COMMAND_INFO + COMMAND_HELP

# variables de control
line : str = ""
command : str = ""
param : str = ""

# ciclo printipal
while command not in COMMAND_EXIT:
    line = input(" > ").lower()

    # buscar el comando
    position : int = 0
    while position < len(line) and line[position] != " ":
        position += 1

    # line[primer_caracter : caracter_final]
    command = line[0:position]

    # buscar el parametro del comando
    position += 1
    offset : int = position
    while position < len(line) and line[position] != " ":
        position += 1

    param = line[offset: position]

    # es solo información de debug para ti :3
    print(f"\t\t\t\t\tDEBUG: [{command}] [{param}]")

    if command in COMMAND_HELP:
        print(HELP_INFO)
        continue

    if command in COMMAND_LIST:
        for index in range(len(agenda)):
            # valido si el primer caracter es #
            if agenda[index][0] == "#":

                # buscamos el nombre
                position = 1
                while agenda[index][position] != " ":
                    position += 1

                print("\t-", agenda[index][1:position])
        continue

    if command in COMMAND_INFO and len(param) > 0:
        db_row : str = ""
        name : str = ""
        index_email : int = -1

        # Buscar el usuario por nombre
        for index in range(len(agenda)):

            name = ""

            # valido si el primer caracter es #
            if agenda[index][0] == "#":

                # buscamos el nombre
                position = 1
                while agenda[index][position] != " ":
                    position += 1

                name = agenda[index][1:position]

            if name == param:
                print(f"\t\t\t\t\tDEBUG: [{agenda[index]}]")

                db_row = agenda[index]

                # buscamos el @ que indica el index del email
                while position < len(db_row):
                    if db_row[position] == "@":
                        index_email = int(db_row[position+1:])
                        break
                    position += 1

                if index_email > 0 and index_email < len(agenda):
                    print("\t-", agenda[index_email][1:])
        continue

    if command in COMMAND_NEW:
        name  : str = input(" name > ")
        mail  : str = input(" mail > ")

        index_name : int  = len(agenda)
        index_email : int = index_name + 1

        print(f"\t\t\t\t\tDEBUG: row name [{index_name}] row mail [{index_email}]")

        agenda.append(f"#{name} @{index_email}")
        agenda.append(f"@{mail}")

