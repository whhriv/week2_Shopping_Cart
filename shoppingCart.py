cart = {}
inventory = {
    'Avacado': 0,
    'Banana': 0,
    'Ceviche': 0,
    'Eggs': 0,
    'Coconut': 0
}
#add a calculator function() to add totals of product

def main():
    while True:
        print('\n\nWelcome to Buenos Rancheros\n\n')
        #print(inventory)
        sel_option = input("Please type \n\n'inventory' to see what is available to add,\n\n 'mycart' to view your shopping cart,\n\n 'remove' to remove items \n\n -----or----\n\n 'quit' to quit at any time:  \n\n\n  : ")  

        if sel_option == 'inventory':
            print('\n\n:')
            print(inventory)  #add formating to style dict
            to_buy = (input('\ntype item to add to cart\n :'))
            cart[to_buy] = cart[to_buy] +1 if to_buy in cart else 1
            print("\n\nyou have added" +' '+ to_buy + ' '+"to cart\n:")   
        elif sel_option == 'mycart':
            print(cart)
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