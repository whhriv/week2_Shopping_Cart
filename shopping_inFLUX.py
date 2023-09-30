# from collections import Counter
cart = {}
inventory = {
    'Avacado': 10,
    'Banana': 12,
    'Ceviche': 5,
    'Eggs': 24,
    'Coconut': 15
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
            to_buy = input('\ntype item to add to cart\n :')
            cart[to_buy] = 1
            
            
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
                removed = cart.pop(del_item)
        elif sel_option == 'quit':
            print('\n\n Your cart: ')
            print(cart)
            print('\n\n')
            break
        else:
            continue
main()

# for key in cart:
#     result = 
# [cart.values + 1 for value in cart]

# def checkKey(cart, key):
#     if key in cart.keys():
#         cart.update({to_buy, +=1})
def add (key):
    if cart.has_key(key):
        cart[key] += 1
    else:
        cart[key] = 1