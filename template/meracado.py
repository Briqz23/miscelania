from string import Template

def Main():


    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=12, qty=1))
    cart.append(dict(item="Fish", price=32, qty=4))

    t = Template("$qty x $item = $price")
    total = 0
    print("Cart: ")
    
    for i in cart: 
        print(t.substitute(i))
        total += i["price"]
    print(f'total = {total}')

if __name__ == '__main__':
    Main()
