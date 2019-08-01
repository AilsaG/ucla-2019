####################### PART ONE #########################
def max(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

    # 1) create a program that checks which input/argument (a or b) is bigger
    # 2) return the bigger value
    ################### YOUR CODE BELOW ######################


    #return 0
    ##########################################################

# Test Cases:
print('max() results below: ')
print(max( 2, 10))
print(max( 4, 4))
print(max( 33, 32))
print(max( -50, -5))
print(max( -1, 0))
print(max( 'james', 'john'))
print(max( '#', '%'))







####################### PART TWO #########################
# 1) create your own function called findMax
# 2) findMax will take a LIST as an input/argument
# 3) use the max function from Part One to find the maximum value in the LIST
# 4) return the max value
# hint: create an empty function first and
# hint: test that you can properly invoke/call the function in part 3

################### YOUR CODE BELOW ######################
def zuida1(aList):

    currentMax = aList[0]  # 5

    for currentItem in aList:
        currentMax = max(currentItem, currentMax)
        


    return currentMax
    
    # v1 = (yi, er, san, si)}
    # for shuzi in 1:
    #     si > san > er > yi



##########################################################









####################### PART THREE #########################
#

##################### EXAMPLE ############################
# We created two functions below called firstFunction() and anotherFunction()
# anotherFunction() uses firstFunction() and then we printed the results
# Feel free to uncomment and run the program below:
#
# def firstFunction(a,b):
#     return [a,b]

# def anotherFunction (someList):
#     return(firstFunction(someList[1], someList[3]))

# print('anotherFunction() results below: ')
# aList = [1,2,3,4]
# b = anotherFunction(aList) 
# print(b)
#
##########################################################
print('findMax() results below: ')
################### YOUR CODE BELOW ######################

#1) Run your findMax/zuida function using the Test Cases below as the inputs
#
# Test Cases:
list1 = [4,2,99,32,50]
list2 = ['mars', 'mark', 'marge', 'marvel', 'mares']
list3 = ['Narwhal', 'Chinese Water Deer', 'Pangolin', 'Bat-eared Fox','Markhor']
list4 = ['Daisy', 'iris', 'Violet', 'poppy', 'Lily'] 


print(zuida1([5,7,6,1,9]))
a = zuida1([4,3,1,8])
print(a)

print(zuida1(list1))
print(zuida1(list2))
print(zuida1(list3))
print(zuida1(list4))






##########################################################










