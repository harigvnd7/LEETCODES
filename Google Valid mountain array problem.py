#here we have to check if the input list is constructed similar to a mountain, that is it strictly increases in value
#initially and from some point until the end of the list it will be strictly decreasing, like the shape of a reversed V

def mountain_check(values : list[int]) -> bool:

        i = 1
        while i < len(values) and values[i] > values[i-1]:
            i+=1


        if (i == len(values) or i == 1):
            return False

        while i < len(values) and (values[i] < values[i-1]):
            i+=1
        if i == len(values):
            return True
        else:
            return False





print(mountain_check([1,2,6,4,6,7,5,3,1]))


