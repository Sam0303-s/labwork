array = [20,50,30,10,60,80]
key = int(input("Enter a key number:  "))

def linear_search(list,k):
    for i in range(len(list)):
        if k == list[i]:
            print("found at ",i+1)
            break

    else:
        print("not found")

linear_search(array,key)