def main():

    list = {}

    while True:
        try:
            type = input().upper()
        except EOFError:
            print()
            for key,value in sorted(list.items()):
                print(value,key)
            break
        else:
            if type in list:
                x = list[type]
                list.update({type: x+1})
            if not type in list:
                list.update({type: 1})

main()