array = [20,50,30,10,60,80]
key = 20

def linear_search(list,k):
    for i in range(len(list)):
        if k == list[i]:
            print("found")

    else:
        print("not found")

linear_search(array,key)