# In this short lesson, we will be going over how to apply logic into your Python code [iteration and selection (and its operators)].
# Iteration - use of for/while loops.
# Selection - use of conditional statements (if, else).
# This lesson should hopefully show you when & where each should be used.


# This section shall be completed using functions rather than writing all code in the main function.
def main():
    print("## Beginning of Lesson-2 ##")

    print("----------------------------------")
    print("### Start of Iteration Section ###")
    iterationExample()
    print("### End of Iteration Section ###")
    print("--------------------------------")



def iterationExample():
    # Whilst programming, you sometimes wish to execute a block of code multiple times (i.e., whilst performing a search/sort).
    # This can be achieved by copy and pasting the code, however what happens if the code has to be repeated a large amount of times? 
    # This would cause the code base to become cluttered and unusable. 
    # As a result of this, we use For and While loops.

    # We will cover data structures in the next lesson, but for now we will define a list of components.
    myList = ['GPU', 'CPU', 'SSD', 'RAM']
    
    # Say I want to display each item in the list once, how could I do this?
    # One option is to simple print each index of the list as such:
    print("--------------------------------")
    print("Bad way start")
    print(myList[0])
    print(myList[1])
    print(myList[2])
    print(myList[3])
    print("Bad way end")
    print("--------------------------------")
    # However, what happens if we have a lis of 1000 items, we will have to write that exact same code 1000 times.
    
    # So instead we use a loop (for/while).

    # Firstly I'll show you one way to do so using a for loop, there are types of for loops (for each, for range).
    # The [for each] loop iterates through every item as an object in the collection.
    # The [for range] loop iterates through every item as an index value instead, the first item is at 0, the second item is at 1, etc.
    # I'll go over both, and you can choose which you prefer.

    print("## For Each Example ##")
    forEachExample()
    print("## For Each End ##")
    print("--------------------------------")
    print("## For Range Example ##")
    forRangeExample()
    print("## For Range End ##")
    print("--------------------------------")
    print("## While Example ##")
    whileExample()
    print("## While End ##")
    
def forEachExample():
    myList = ['Apple', 'Pear', 'Apricot', 'Lychee']
    # The logic for the for loop reads as such:
    # For each [item] in [myList], call the print the item.
    for item in myList:
        print(item)

def forRangeExample():
    myList = ['Word', 'Excel', 'PowerPoint', 'Publisher']
    # The logic for the for range reads as such:
    # For index in range of the length of the list, print the item at index in the collection.
    # Essentially, the loop iterates from 0 to the length of the list - 1.
    for index in range(len(myList)):
        print(myList[index] + " is at index " + str(index)+ " in the list")               

def whileExample():
    myList = ['Red', 'Yellow', 'Green', 'Blue']
    counter = 0
    # The logic of the while loop reads as so:
    # While the counter is less than the length of the list, print the item in the list at index counter, and then increment the value of counter.
    while (counter < len(myList)):
        print(myList[counter])
        counter += 1

def selectionExample():
    return 0

main()
