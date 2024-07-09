# Basic Python data structures:
# 1. Lists
# 2. Tuples
# 3. Sets
# 4. Dictionaries

# These data structures are classes defined in python and
# we use them by creating objects of those classes.

def main() -> None:
    # For example, myList below is an object of class "List"
    # -- Lists --
    # A List contains a series of objects of the SAME type separated by commas.
    myList = [1, 2, 3] # We initialize a List object with brackets []
    myList[1] = 5      # A List object is MUTABLE, which means that we can change
                       # the values of its elements at any time.

    # -- Tuples --
    # A Tuple contains a series of objects of DIFFERENT type,separated by commas.
    myTuple = (2, "hello", myList) # We initialize a Tuple object with parentheses ()
                                   # A Tuple object is IMMUTABLE, which means that
                                   # we cannot change its elements after initialization
    print(myTuple[2])
    #myTuple[0] = 1 -> ERROR: 'tuple' object does not support assignment

    # -- Sets --
    # A Set contains a collection of NO DUPLICATE elements of the SAME type, separated by commas.
    mySet = {"orange", "apple", "banana"} # We initialize a Set object with curly brackets {}
                                          # A Set object is IMMUTABLE, which means that
                                          # we cannot change its elements after initialization
    print(mySet)
    #mySet[0]="pineapple" -> ERROR: 'set' object does not support assignment

    setDemo = {1, 1, 2, 2, 3, 3}
    print(setDemo)

    # --Dictionaries --
    # A Dictionary is a set of KEY:VALUE pairs.
    # The KEY and the corresponding OBJECT can be of any type.
    myDict = {"costas": 4056, "katerina": 5092} # We initialize a Dictionary object with curly
                                                # brackets. Being essentially a Set of KEY:VALUE pairs
                                                # a Dictionary is also IMMUTABLE.
    print(myDict) # Prints all key:value pairs
    print(myDict["costas"]) # We access the element of a Dictionary through its key

if __name__ == "__main__":
    main()
