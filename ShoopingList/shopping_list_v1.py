shopping_list = {}


def view_list():
    if len(shopping_list) == 0:
        print("A sua lista de compras está vazia.\n")
    else:
        for item, qty in shopping_list.items():
            print(f"{item} - {qty}")


def add_item():
    item = input("Introduza o item a comprar: \n")
    qty = input("Introduza a quantidade a comprar: ")
    if qty == "":
        qty = 1
    shopping_list[item] = qty
    print("Item adicionado com sucesso.")
    
def change_item():
    item = input("Indique o item a alterar:\n")
    if item in shopping_list:
        qty = input("Introduza a nova quantidade a alterar: ")
        shopping_list.update({item:qty})
    else:
        answer = input("O item não existe na sua lista. Quer adiciona? [S/N]").upper()
        if answer == "S":
            qty = input("Introduza a nova quantidade a alterar: ")
            if qty == "":
                qty = 1
            shopping_list[item] = qty
        


while True:
    print("---------- APP DE COMPRAS -----------")
    print("""
         ------------ MENU -----------
          1 - Mostrar lista 
          2 - Inserir item 
          3 - Alterar item
          0 - Sair \n
          """)
    
    option = None
    
    option = int(input("Escolha a sua opção: "))

    if option == 1:
        view_list()
    elif option == 2:
        add_item()
    elif option == 3:
        change_item()
    else:
        quit()

