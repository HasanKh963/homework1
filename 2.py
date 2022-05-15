while True:
    d=int(input('enter a number'))
    binary=[]
    while True:
        binary.append(str(d%2))
        d//=2
        if d:
            continue
        else:
            break
    print("we are reversing the list now")
    binary.reverse()
    binary=''.join(binary)
    print(binary)
    print("continue, y or n")
    s=input()
    if s!='y':
        break