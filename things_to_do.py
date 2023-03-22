#https://culturedcode.com/things/support/articles/2803573/


def to_do_generator():

    #    project_name = input("Project title: ").replace(" ","_")
    #    to_do_name = input("To-Do name: ").replace(" ","_")
    #    tag_name = input("Tag name: ").replace(" ","_")
    #    initial_number = int(input("First number: "))
    #    final_number = int(input("Final number: "))

    # **********************
    project_name = 'JS_NodeJS'  # Não deixe espaço em branco
    to_do_name = 'Aula'
    initial_number = 1
    final_number = 26
    # **********************

    project_default = "things:///add-project?title="
    to_do_default = "to-dos="
    #tag_name = 'tags='
    to_dos = ""

    result = f'{project_default}{project_name}&{to_do_default}'

    for number in range(initial_number, final_number + 1):
        to_dos = f'{to_dos}{to_do_name}{str(number)}%0A'
    return result + to_dos


print(to_do_generator())