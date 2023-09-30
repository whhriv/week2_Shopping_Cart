cart = {}
inventory = {
    'Avacado': 1,
    'Banana': 1,
    'Ceviche': 1,
    'Eggs': 1,
    'Coconut': 1
}
#add a calculator function() to add totals of product

def main():
    while True:
        print('\n\nWelcome to Buenos Rancheros\n')
        sel_option = input("OPTIONS: \n\n' Type: inventory' to view inventory and to ADD,\n\n Type: 'mycart' to view your shopping cart,\n\n Type: 'remove' to remove items \n\n -----or----\n\n  Type: 'quit' to quit at any time:  \n\n\n  : ")  

        if sel_option == 'inventory':
            print('\n\n:')
            print(inventory)  
            to_buy = (input('\n Input item to add to cart\n :'))
            cart[to_buy] = cart[to_buy] +1 if to_buy in cart else 1
            print("\n\nyou have added" +' '+ to_buy + ' '+"to cart\n:")   
        elif sel_option == 'mycart':
            print('\n\n Current Cart:')
            print(cart)
            print('\n\n')
        elif sel_option == 'remove':
            print(cart)
            del_item = input('\nplease type name of item to remove:\n :')
            if del_item not in cart:
                print("\n\nYou don't have that item!!!\n\n")
            else:
                cart[to_buy] = cart[to_buy] -1 if to_buy in cart else cart.pop(del_item)   
        elif sel_option == 'quit':
            print('\n\n Your cart: ')
            print(cart)
            print('\n\n Total: ')
            receipt = sum([i  for i in cart.values()])
            print( receipt*1.01)
            print(float(receipt)*1.00)
            break
        else:
            continue
main()