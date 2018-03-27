# NDList
Helps working with lists of unknown dimensionality

# Loop through the list
  ```Python
  for loopIndex, value in NDList.Iterator(testList):
      print(loopIndex, value)
      
  [0, 0, 1] 0
  [0, 1, 0] 1
  [0, 1, 1] 2
  [1, 0, 0] 3
  [1, 0, 1] 4
  [1, 1, 0] 5
  [1, 1, 1] 6
  [1, 1, 1] 7    
  ```
  
  

# Create a list of specified dimensionality with speciefied rows per dimension
  ```Python 
  NDList.createNDList([1, 2, 2])
  print(NDList(NDList.createNDList([1, 2, 2]))) ->
  [ 
    [ 
      [0, 0]
      [0, 0]
    ] 
  ] 
```

<br/>
<br/>

```Python 
testList =  [                     
              [[0, 1], [2, 3]],   
              [[4, 5], [6, 7]]    
            ]                     
```
            
# Flats out all dimensions to one
  ```Python 
  print(NDList.flattnList(testList)) -> [0, 1, 2, 3, 4, 5, 6, 7]                    
  ```
  
<br/>
<br/>

# Get's the dimensions of the list with the amount of rows
  ```Python 
  print(getListDimensions(testList))      -> [2, 2, 2]   = 2 rows in every dimension 
  print(len(getListDimension(testList)))  -> 3           = 3 Dimensions              
  ```
  
<br/>  
<br/>

# Get's an item from the specified index
  ```Python 
  print(NDList.getItem(testList, [0, 1, 1])) -> 3      
  ```


<br/>
<br/>


# Sets an item in the list at a specified index
  ```Python 
  NDList.setItem(testList, [0, 1, 1], 100)                                            
  print(NDList.getItem(testList, [0, 1, 1])) -> 100                                  
  ```
  
 <br/>
 <br/>
 
 # Add a row to the specified dimension index
 ```Python 
  NDList.addRowToDimension(testList, 1)                                               
  print(NDList.getListDimensions(testList))        -> [2, 3, 2]                      
  ```
  

<br/>
<br/>


# Remove a row from the specified dimension index
  ```Python 
 NDList.removeRowFromDimension(testList, 1)                                           
 print(NDList.getListDimensions(testList))        -> [2, 1, 2]                       
 ```
 
 
 <br/>  
 <br/>  
 
 
 # Inserts a dimension to a list while keeping the same substructure
  ```Python 
  NDList.insertDimensionToList(testList, 2, 2)                                        
  print(NDList.getListDimensions(testList))        -> [2, 2, 3, 2]                     

    [                   
      [                 
        [               
          [0, 1],      
          [0, 1]       
        ],              
        [               
          [2, 3],       
          [2, 3]        
        ]               
      ],                 
      [                 
        [                
          [4, 5],       
          [4, 5]         
        ],              
        [               
          [6, 7],      
          [6, 7]        
        ]               
      ]                 
    ]                   
  ```
  <br/>  
  <br/>  
  
  
  # Removes a dimension from a list 
    ```Python 
    NDList.removeDimensionFromList(testList, 2)                                      
    print(NDList.getListDimensions(testList))        -> [4, 2]                     
                                                        
    [               
      [0, 1],       
      [2, 3],       
      [4, 5],       
      [6, 7],       
    ]               
    ```
 <br/> 
 <br/> 
 
 # Apply a function on every element
  ```Python 
   def func(val):
      print(val)
   NDList.applyFunction(testList, func)          -> prints all elements out
   ```
   
