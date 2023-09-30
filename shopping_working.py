cart = {}
inventory = {
    'Avacado': 10,
    'Banana': 12,
    'Ceviche': 5,
    'Eggs': 24,
    'Coconut': 15
}

def main():
    while True:
        print('Welcome to Buenos Rancheros\n\n\n')
        print(inventory)
        sel_option = input("Please type 'inventory' to see what we have in stock, 'mycart' to view your shopping cart, 'remove' to remove items or 'quit' to quit at any time:  \n\n\n  : ")  
        print("          :")
        if sel_option == 'inventory':
            print(inventory)  #add formating to style dict
            to_buy = input('type item to add to cart\n :')
            cart[to_buy] = '1'
            print("you have added" +' '+ to_buy + ' '+"to cart\n:")       
        elif sel_option == 'mycart':
            print(cart)
        elif sel_option == 'remove':
            print(cart)
            del_item = input('please type name of item to remove:\n :')
            if del_item not in cart:
                print("You don't have that item")
            else:
                removed = cart.pop(del_item)
        elif sel_option == 'quit':
            print(cart)
            break
        else:
            continue
main()