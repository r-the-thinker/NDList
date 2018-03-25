
#from NDList_iterator import *

class NDList:

    # # # # # # # # # # # # #
    #   Static Functions    #
    # # # # # # # # # # # # #

    # Function Overview:
    # -> createNDList([2, 2, 2])
    # -> flattnList(targetList)
    # -> getListDimensions(targetList)
    # -> getItem(targetList, indecies)
    # -> setItem(targetList, indecies, value)
    # -> addRowToDimension(targetList, indexOfDimension)
    # -> removeRowFromDimension(targetList, indexOfDimension)
    # -> insertDimensionToList(targetList, indexOfDimension, rowsToCreate)
    # -> removeDimensionFromList(targetList, indexOfDimension)
    # -> applyFunction(targetList, functionToApply)



    # Creates A Multidimensional List Based On The Paramters
    # @Params:  -dimensions = a list describing the dimensions
    #                         [2, 2, 2] would create a 3D List
    #                         made up of lists witch each 2 sublists
    #           -depth is used for recusion so initially 0
    # @Return:  -A Multidimensional List
    @staticmethod
    def createNDList(dimensions):
        # Early Error Catching:
        if len(dimensions) == 0:
            return []

        # Do The Recursion
        return NDList._createNDList(dimensions, 0)


    # USED INTERNALLY
    # Creates A Multidimensional List Based On The Paramters
    # @Params:  -dimensions = a list describing the dimensions
    #                         [2, 2, 2] would create a 3D List
    #                         made up of lists witch each 2 sublists
    #           -depth is used for recusion so initially 0
    # @Return:  -A Multidimensional List
    @staticmethod
    def _createNDList(dimensions, depth):

        # defines what to do on the data level
        if len(dimensions)-1 == depth:
            return [0 for x in range(dimensions[-1])]

        # creates the parent list that holds inner lists
        subLists = []
        for i in range(dimensions[depth]):
            subLists.append(NDList._createNDList(dimensions, depth+1))
        return subLists


    # Reduces N Dimensions To 1
    # @Params:  -targetList = the list to boil down
    # @Return:  -the fattend list
    @staticmethod
    def flattnList(targetList):
        # Early Error Catching:
        if len(targetList) == 0:
            return []

        # Do The Recursion
        return NDList._flattnList(targetList)

    # USED INTERNALLY
    # Reduces N Dimensions To 1
    # @Params:  -targetList = the list to boil down
    # @Return:  -the fattend list
    @staticmethod
    def _flattnList(targetList):
        # Is The Content Of The List Data Return The Itself
        if not isinstance(targetList[0], list):
            return targetList

        # Otherwise Create A Parent List And Join Flattend Sublists Together
        lists = []
        for l in targetList:
            lists += NDList._flattnList(l)
        return lists



    # Returns The Content At That Position
    # @Params:  -targetList = the list to use
    #           -indecies   = e.g. [2, 2, 2] means look for the item in the
    #                         second list of the second list
    # @Return:  -an item
    @staticmethod
    def getItem(targetList, indecies):
        # Early Error Catching:
        if len(targetList) == 0:
            raise Exception("Can't return an item from an empy list")

        # Do The Recusion
        return NDList._getItem(targetList, indecies, 0)


    # USED INTERNALLY
    # Returns The Content At That Position
    # @Params:  -targetList = the list to use
    #           -indecies   = e.g. [2, 2, 2] means look for the item in the
    #                         second list of the second list
    #           -depth is used for recusion and initially 0
    # @Return:  -an item
    @staticmethod
    def _getItem(targetList, indecies, depth):
        # If It Is The Last Dimension Return The Content At That Position
        if len(indecies)-1 == depth:
            # Error Catching:
            if isinstance(targetList[0], list):
                raise Exception("The specified indecies don't point to a value but a list")

            # Return The Item
            return targetList[indecies[depth]]

        # Error Catching:
        if not isinstance(targetList[0], list):
            raise Exception("The specified indecies overstep the dimensions of the list")

        # Otherwise Go Deeper And Ask The Inner List To Get It's Content
        return NDList._getItem(targetList[indecies[depth]], indecies, depth +1)



    # Set The Content At That Position To A Specific Value
    # @Params:  -targetList = the list to search
    #           -indecies   = e.g. [2, 2, 2] means use the item in the
    #                         second list of the second list
    #           -value      = the value to set the list index to
    # @Return:  -void
    @staticmethod
    def setItem(targetList, indecies, value):
        # Early Error Catching:
        if len(targetList) == 0:
            raise Exception("Can't set an item in a empty list")

        # Do The Recursion
        NDList._setItem(targetList, indecies, value, 0)


    # USED INTERNALLY
    # Set The Content At That Position To A Specific Value
    # @Params:  -targetList = the list to search
    #           -indecies   = e.g. [2, 2, 2] means use the item in the
    #                         second list of the second list
    #           -value      = the value to set the list index to
    #           -depth is used for recusion and initially 0
    # @Return:  -void
    @staticmethod
    def _setItem(targetList, indecies, value, depth):
        # If It Is The Last Dimension Set The Value At That Position In The List
        if len(indecies)-1 == depth:
            # Error Catching:
            if isinstance(targetList[0], list):
                raise Exception("The specified indecies don't point to a value but a list")
            # Set The Value
            targetList[indecies[depth]] = value
            return

        # Error Catching:
        if not isinstance(targetList[0], list):
            raise Exception("The specified indecies overstep the dimensions of the list")

        # Otherwise Go Deeper And Ask The Inner List To Get It's Content
        NDList._setItem(targetList[indecies[depth]], indecies, value, depth+1)


    # Gives The Dimensions Of A List Of Unspecified Dimensions
    # @Params:  -targetList = the list to use
    # @Return:  -a list containing the dimensions
    #            [2, 2] -> means 2 Dimensions with each 2 rows
    @staticmethod
    def getListDimensions(targetList):
        # Earyl Error Catching;
        if len(targetList) == 0:
            return []
        # Do The Actual Recursion
        return NDList._getListDimensions(targetList)

    # USED INTERNALLY
    # Gives The Dimensions Of A List Of Unspecified Dimensions
    # @Params:  -targetList = the list to use
    # @Return:  -a list containing the dimensions
    #            [2, 2] -> means 2 Dimensions with each 2 rows
    @staticmethod
    def _getListDimensions(targetList):
        # Is The Content Of This A List Then Go Deeper
        if isinstance(targetList[0], list):
            return [len(targetList)] + NDList._getListDimensions(targetList[0])

        # If It Is The End Return The Length Of The Current Target List
        return [len(targetList)]


    # Adds Another Row To The Specified Dimension
    # @Params:  -targetList = the list to modify
    #           -targetDimensionIndex = the dimensions to add more to
    # @Return:  -void
    @staticmethod
    def addRowToDimension(targetList, targetDimensionIndex):
        # Early Error Catching:
        if len(targetList) == 0:
            raise Exception("Can't add a row to an empy list")
        if targetDimensionIndex < 0:
            raise Exception("Can't add a row to target dimension: " + str(targetDimensionIndex))

        dimensionsOfList = NDList.getListDimensions(targetList)
        if len(dimensionsOfList)-1 <= targetDimensionIndex:
            raise Exception("Can't add a row on the data level -> (len(getListDimensions(targetList)) = "
                            + str(len(dimensionsOfList)) + ") is equal to (targetDimensionIndex = "
                            + str(targetDimensionIndex) + ")")

        # Do The Actual Recursion
        NDList._addRowToDimension(targetList, targetDimensionIndex, dimensionsOfList, 0)

    # USED INTERNALLY
    # Adds Another Row To The Specified Dimension
    # @Params:  -targetList = the list to modify
    #           -targetDimensionIndex = the dimensions to add more to
    #           -dimensions  = the list of all dimensionss of that n d list
    #           -depth for recursion initially 0
    # @Return:  -void
    @staticmethod
    def _addRowToDimension(targetList, targetDimensionIndex, dimensions, depth):

        # Create Sublists With The Same Structure As The Others And Add It As Row
        # To The Target Dimension
        if depth == targetDimensionIndex:
            # Create SubLists With Same Structure And Add Them
            subLists = NDList.createNDList(dimensions[depth+1:])
            targetList.append(subLists)
            return

        # go deeper in all sub lists until the desired dimention is reached
        for innerList in targetList:
            NDList._addRowToDimension(innerList, targetDimensionIndex, dimensions, depth+1)



    # Removes A Row From The Specified Dimension
    # @Params:  -targetList = the list to modify
    #           -targetDimensionIndex = the dimention where a row should be removed
    # @Return:  -void
    @staticmethod
    def removeRowFromDimension(targetList, targetDimensionIndex):
        # Early Error Catching:
        if len(targetList) == 0:
            raise Exception("Can't remove row if list is empty")
        if targetDimensionIndex < 0:
            raise Exception("Can't remove row in target dimension: " + str(targetDimensionIndex))

        # Do The Actual Recursion
        NDList._removeRowFromDimension(targetList, targetDimensionIndex, 0)


    # USED INTERNALLY
    # Removes A Row From The Specified Dimension
    # @Params:  -targetList = the list to modify
    #           -targetDimensionIndex = the dimention where a row should be removed
    #           -depth is used for recursion initially 0
    # @Return:  -void
    @staticmethod
    def _removeRowFromDimension(targetList, targetDimensionIndex, depth):
        # In The Parent Of The Desired Dimension Loop Through All Children
        # To Remove Their Last Child

        if depth == targetDimensionIndex:
            # Error Catching:
            if not isinstance(targetList, list):
                raise Exception("Choose a dimension that has sublists to remove")
            # Remove The Last Element From The List
            targetList.pop()
            return

        # Go Deeper on all subLists
        for innerList in targetList:
            NDList._removeRowFromDimension(innerList, targetDimensionIndex, depth+1)


    # Inserts A New Dimension To The Specified Depth
    # @Params:  -targetList = the list to modify
    #           -targetDimensionIndex = the dimension where to create a new one at
    #           -rowsOfNewDimension = amount of rows to be added to the inserted dimension
    #           -depth is used for recursion initially 0
    # @Return:  -void
    @staticmethod
    def insertDimensionToList(targetList, targetDimensionIndex, rowsOfNewDimension):
        # Early Error Catching:
        if targetDimensionIndex < 0:
            raise Exception("Can't insert to " + str(targetDimensionIndex) + " dimension")
        if rowsOfNewDimension < 1:
            raise Exception("Can't create " + str(rowsOfNewDimension) + " many rows")
        # Do The Actual Recursion
        NDList._insertDimensionToList(targetList, targetDimensionIndex, rowsOfNewDimension, 0)

    # USED INTERNALLY
    # Inserts A New Dimension To The Specified Depth
    # @Params:  -targetList = the list to modify
    #           -targetDimensionIndex = the dimension where to create a new one at
    #           -rowsOfNewDimension = amount of rows to be added to the inserted dimension
    #           -depth is used for recursion initially 0
    # @Return:  -void
    @staticmethod
    def _insertDimensionToList(targetList, targetDimensionIndex, rowsOfNewDimension, depth):
        # If Dove Deep Enough, Make A Copy Of The Sublists, Clear Current Lists,
        # Add Rows To That Dimension, Add Saved Sublists To The Rows

        if depth == targetDimensionIndex:
            # Error Catching
            if not isinstance(targetList, list):
                raise Exception("Can't insert a new dimension on the data level")

            # Encapsulate In New List
            save = list(targetList)
            targetList.clear()
            for l in range(rowsOfNewDimension):
                targetList.append(list(save))
            return

        # Dive Deeper On All Sublists
        for innerList in targetList:
            NDList._insertDimensionToList(innerList, targetDimensionIndex, rowsOfNewDimension, depth+1)


    # Removes A Dimension From At A Specified Depth
    # @Params:  -targetList = list to modify
    #           -targetDimensionIndex = the dimension to be removed
    # @Return:  -void
    @staticmethod
    def removeDimensionFromList(targetList, targetDimensionIndex):
        # Early Error Catching
        if targetDimensionIndex == 0:
            raise Exception("Can't Remove The First Dimension")
        # Do The Recursion
        NDList._removeDimensionFromList(targetList, targetDimensionIndex, 0)

    # USED INTERNALLY
    # Removes A Dimension From At A Specified Depth Except 0
    # @Params:  -targetList = list to modify
    #           -targetDimensionIndex = the dimension to be removed
    #           -depth for recursion initially 0
    # @Return:  -void
    @staticmethod
    def _removeDimensionFromList(targetList, targetDimensionIndex, depth):
        # Is It The Parent Of The Desired Dimension
        if depth == targetDimensionIndex-1:
            # Early Error Catching
            if not isinstance(targetList[0][0], list):
                raise Exception("Can't remove a row on the data level")

            # Save Sublists Of Target Dimensions
            targetDimensionSave = [list(subList) for innerList in targetList for subList in innerList ]
            # Remove All From Parent
            targetList.clear()
            # Add All Saved Sublists To The Parent
            for saved in targetDimensionSave:
                targetList.append(saved)
            return

        # Go Deeper
        for l in targetList:
            NDList._removeDimensionFromList(l, targetDimensionIndex, depth+1)


    # Applies A Function On The Data
    # @Params:  -targetList = the list to go over
    #           -function = the function to apply
    # @Return:  -void
    @staticmethod
    def applyFunction(targetList, function):
        # Early Error Catching:
        if len(targetList) == 0:
            raise Exception("Can't applyFunction a function to an empty list")

        return NDList._applyFunction(targetList, function, 0)

    # USED INTERNALLY
    # Applies A Function On The Data
    # @Params:  -targetList = the list to go over
    #           -function = the function to apply
    #           -depth = used for recursion initially 0
    # @Return:  -void
    @staticmethod
    def _applyFunction(targetList, function, depth):
        # if it is the list containing data apply the function on it
        if not isinstance(targetList[0], list):
            for data in targetList:
                function(data)
            return

        # Otherwise Go Deeper In All Sublists
        for l in targetList:
            NDList._applyFunction(l, function, depth+1)


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


    # # # # # # # # # # # # #
    #   Class Definition    #
    # # # # # # # # # # # # #


    def __init__(self, data = None, dimensions = None):
        if not data == None:
            self.data = data
            self.dimensions = NDList.getListDimensions(data)
        elif not dimensions == None:
            self.data = NDList.createNDList(dimensions)
            self.dimensions = dimensions


    def __iter__(self):
        return NDList.Iterator(self.data)

    def __str__(self):
        return self._toString(self.data)


    # Overrides get function to return an item in the specified location
    # @Usage: nameOfList[ indecies ] -> nameOfList[ [1, 1, 0] ]
    # @Params:  -indecies = list of integers pointing to the data
    # @Return:  -data at that location
    def __getitem__(self, indecies):
        return NDList.getItem(self.data, indecies)

    # Overrides set function to set a item in the specified location
    # @Usage: nameOfList[ indecies ] = value-> nameOfList[ [1, 1, 0] ] = 10
    # @Params:  -indecies = list of integers pointing to the data
    #           -value = the value to set that position to
    # @Return: void
    def __setitem__(self, indecies, value):
        NDList.setItem(self.data, indecies, value)

    # Returns a list that contains
    # the amount of rows for each dimension
    def getDimensions(self):
        return NDList.getListDimensions(self.data)

    # Adds A Row To The Specified Dimension
    def addRow(self, targetDimensionIndex):
        NDList.addRowToDimension(self.data, targetDimensionIndex)

    # Removes A Row From The Specified Dimension
    def removeRow(self, targetDimensionIndex):
        NDList.removeRowFromDimension(self.data, targetDimensionIndex)

    # Inserts A New Dimension With The Specified Amount Of Rows
    # In To The Specified Dimension While Keeping The Previous
    # Substructure
    def insertDimension(self, targetDimensionIndex, amountOfRows):
        NDList.insertDimensionToList(self.data, targetDimensionIndex, amountOfRows)

    # Removes The Specified Dimension While Keeping The Substructure
    def removeDimension(self, targetDimensionIndex):
        NDList.removeDimensionFromList(self.data, targetDimensionIndex)

    # Applies A Function To Values In The List
    def apply(self, function):
        NDList.applyFunction(self.data, function)

    # Reduces N Dimensions To 1
    def flattn(self):
        return NDList.flattnList(self.data)

    # Usedd Internally for recursion
    def _toString(self, innerList, depth = 0):
        buff = '[ \n'

        # Is The Content Not A List
        if not isinstance(innerList[0], list):
            return innerList.__str__()

        for l in innerList:
            buff += '\t'*(depth+1) + self._toString(l, depth = depth+1) + '\n'

        buff += '\t'*depth + '] \n'
        return buff




    # # # # # # # # # # # # #
    # Iterator For ND Lists #
    # # # # # # # # # # # # #


    class Iterator:

        def __init__(self, data):
            # Take The List Object And Get It's Dimensions
            self.data = data
            self.dimensions = NDList.getListDimensions(data)

            # Reset The Loop Index
            self.loopIndex = [0 for x in range(len(self.dimensions))]
            # Max To Iterate to
            self.maxLoopIndex = [x-1 for x in self.dimensions]
            # Put List Pointer To The First Value
            self._jumpTo(self.data, list(self.loopIndex))
            # The Flag If The Iteration Is Finished
            self.isFinished = False
            # Return The Iterator Object

        def __iter__(self):
            '''
                Called by the for loop to create an iterator
                (something that implemented next())
            '''
            return self

        def __next__(self):
            ''' Called by the for loop to get he data '''

            # When The Max Loop Index Is Overstepped Raise The Stop Iteration
            if self.isFinished:
                raise StopIteration()

            # Set The Flag If The Last Item Is Reached
            if self.loopIndex == self.maxLoopIndex:
                self.isFinished = True

            # Get The Value For The Index
            returnValue = self.innerList
            returnLoopIndex = self.loopIndex

            # Only If It Is Not Finished Get The Next Index
            if not self.isFinished:
                # Increase The Loop Index And Manage The Correct Size
                self._getNext()
                # Set The InnerList Pointer To The New LoopIndex
                self._jumpTo(self.data, list(self.loopIndex))

            # Return The Values To Be Received In The Loop
            return returnLoopIndex, returnValue


        def _resetListIndex(self, targetList):
            ''' Jumps To The First value Element In The List '''
            if not isinstance(targetList[0], list):
                self.innerList = targetList
                return
            self._resetListIndex(targetList[0])

        def _getNext(self):
            ''' Manages The Loop Index '''
            # Count Up The Highest Dimension
            self.loopIndex[-1] += 1

            # Check From Highest To Lowest If The Index Is As Big As The Dimension
            # That Means That There Are No More Rows In That Dimension
            # Therefore Count Up The Lower Dimension And Zero Out All Following
            # The For Loop Starts At The End And Corrects The LoopIndex Iteration By Iteration
            for loopPos, maxLoopPos in zip(range(len(self.loopIndex)-1, -1, -1), range(len(self.maxLoopIndex)-1, -1, -1)):
                # Only Do The Correction If It Is Not Allready The Lowest Dimension
                if self.loopIndex[loopPos] > self.maxLoopIndex[maxLoopPos]:
                    if not loopPos == 0:
                        # Count Up On The Lower Dimension
                        self.loopIndex[loopPos-1] += 1
                        # Null Out The Higher Dimensions
                        for i in range(loopPos, len(self.loopIndex)):
                            self.loopIndex[i] = 0


        def _jumpTo(self, subList, indecies):
            if not len(indecies) == 0:
                self._jumpTo(subList[indecies.pop(0)], indecies)
            else:
                self.innerList = subList
