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
        # ask = input('Pleast type quit to quit')
        # if ask == 'quit':
        #     break
        # else:
        #     continue
        print('Welcome to Buenos Rancheros')
        print(inventory)
        sel_option = input("Please type 'inventory' to see what we have in stock, 'mycart' to view your shopping cart, 'remove' to remove items or 'quit' to quit at any time")
        
        
        if sel_option == 'inventory':
            print(inventory)  #add formating to style dict
            to_buy = input('type item to add to cart: ')
            cart[to_buy] = '1'
            
            
        elif sel_option == 'mycart':
            print(cart)
        elif sel_option == 'remove':
            print(cart)
            del_item = input('please type name of item to remove: ')
            removed = cart.pop(del_item)

        elif sel_option == 'quit':
            break
        else:
            continue
main()