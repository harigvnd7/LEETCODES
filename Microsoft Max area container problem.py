#the following problem asks the user to input a list of heights and then find the max area of an imaginary container
#that is conscribed by the entries of the list taken as walls of height and the index position of each entry will be the width

def area_container(heights : list[int]) -> int:
    max_area = 0
    x = 0
    y = len(heights)-1
    while x<y:
        width = abs(x-y)
        length = min(heights[x],heights[y])
        area = width * length
        if area > max_area:
            max_area = area
        if heights[x] <= heights[y]:
            x += 1
        else:
            y -= 1
    return max_area


print(area_container([7,4,3,13,20,1,8]))

'''this can also be done using 2 for loops but that is more complex'''