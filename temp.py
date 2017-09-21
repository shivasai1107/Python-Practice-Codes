from string import Template


def main():
    cart=[]
    cart.append(dict(item="shit",price=12))
    cart.append(dict(item="shit1",price=1))

    t= Template("$item * $price ")

    total=0
    
    print "cart"
    for data in cart:
        print t.substitute(data)
        total += data["price"]
    print "Total"+str(total)

if __name__=="__main__":
    main()
