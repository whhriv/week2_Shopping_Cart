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
        print('\n\n\nWelcome to Buenos Rancheros\n\n\n')
        #print(inventory)
        sel_option = input("Please type 'inventory' to see what is available to add,\n\n 'mycart' to view your shopping cart,\n\n 'remove' to remove items \n\n -----or----\n\n 'quit' to quit at any time:  \n\n\n  : ")  

        if sel_option == 'inventory':
            print('\n\n:')
            print(inventory)  #add formating to style dict
            to_buy = (input('\ntype item to add to cart\n :'))
            # for i in cart:
            #     if [to_buy] == cart.keys():
            # if to_buy not in inventory.values():
            #     print('We do not have')
            #     main()
            # else:
            #     continue
            
            cart[to_buy] = cart[to_buy] +1 if to_buy in cart else 1

            # if to_buy in inventory:
            #     cart[to_buy] = cart[to_buy] +1 if to_buy in cart else 1
            # else:
            #     print('NOT AVAILABLE')
            #^^^ CHANGE ABOVE
            
            # if cart[to_buy] is not None:
            #     cart[to_buy] += 1
            # else:
            #    cart.setdefault(to_buy, 0)
            #    cart[to_buy] += 1
                # cart[to_buy] = cart.get(to_buy, 0) +1
                # cart[to_buy] += 1  
            print("\n\nyou have added" +' '+ to_buy + ' '+"to cart\n:")   
  
        #elif sel_option == *args
        
        elif sel_option == 'mycart':
            print(cart)
        elif sel_option == 'remove':
            print(cart)
            
            del_item = input('\nplease type name of item to remove:\n :')
            if del_item not in cart:
                print("\n\nYou don't have that item!!!\n\n")
            else:
                # while cart[to_buy] > 0:
                cart[to_buy] = cart[to_buy] -1 if to_buy in cart else cart.pop(del_item) 
                # removed = cart.pop(del_item)
                # receipt = [i for i in cart.values()]    
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
    # receipt = [sum(i) for i in cart.values()]
main()