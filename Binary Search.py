#This function()  is  Binary Search
# 19:10 11.02.2022  Author : DKing
#It was learned from the Book Grokking Algorithms


#create a function()   binary-search :
def binary_search(list,item):
    low = 0
    heigh = len(list)-1

    while( low <= heigh ):

        #find a middle part
        middle =  low + heigh

        #To Guess
        supposition = list[middle]

        # Compare the result with item
        # if the  result match with item
        # function return the result
        if supposition == item :
            return middle

        if supposition > item :
            # change HEIGH position
            heigh = middle - 1

        else :
            #change LOW position
            low = middle + 1

    #if the function can't find in the list.
    # it's return none
    return None

#items in the list , you have can rewritten
list_items= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#Test To work
print(binary_search(list_items , 12))
