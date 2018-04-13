# Kang Sheng's algorithm homework.


## 1.Sort Method Compare

### 1.Environment

	Ubuntu 17.10 
	Python 3.6.4
	
### 2.File: 

#### /sort/convention.py

Three convention sort methods, whose time complexity is O(n^2). They are bubble sort, insert sort and select sort.

#### /sort/advanced.py

Four advance sort methods, whose time complexity is O(nlgn). They are built-in sort, merge sort, heap sort and quick sort.

#### /sort/main.py

Quoting convention.py and advanced.py to calculate time consumed and plot  a picture.

### 3.Usage

	cd ./sort
	python3 main.py
	
### 4.Output

The result include time consumed for each sort method and a picture.

	Initial numbers succeed! There are 200 numbers in total.
	Function Bubble succeeded! cost 0.00459 seconds.
	Function Insert succeeded! cost 0.00202 seconds.
	Function Select succeeded! cost 0.00153 seconds.
	Function Heap succeeded! cost 0.00124 seconds.
	Function Merge succeeded! cost 0.00073 seconds.
	Function Quick succeeded! cost 0.00037 seconds.
	Function BuiltIn succeeded! cost 4.00000 seconds.
	...
	Initial numbers succeed! There are 100000 numbers in total.
	It will take too long for basic sort method Bubble.
	It will take too long for basic sort method Insert.
	It will take too long for basic sort method Select.
	Function Heap succeeded! cost 1.50281 seconds.
	Function Merge succeeded! cost 0.78786 seconds.
	Function Quick succeeded! cost 0.44708 seconds.
	Function BuiltIn succeeded! cost 0.04711 seconds.
	
![Alt result](https://raw.githubusercontent.com/techkang/alo/master/sort/result.png)
## 2.Nearnest Neighbor
### 1.File
#### /sort/nn/main.py
The only python file for nearnest neighbor, it can calculate the nearest distance of all the pairs by divide-and-conquer method.
### 2.Usage
	cd alo/nn
    python3 main.py
### 3.Output
	Total numbers: 10, time elapsed: 0.00016
    Total numbers: 20, time elapsed: 0.00052
    Total numbers: 40, time elapsed: 0.00124
    Total numbers: 80, time elapsed: 0.00652
    Total numbers: 160, time elapsed: 0.01087
    Total numbers: 320, time elapsed: 0.02149
    Total numbers: 640, time elapsed: 0.05532
    Total numbers: 1280, time elapsed: 0.29359
    Total numbers: 2560, time elapsed: 1.94292
    Total numbers: 5120, time elapsed: 39.6151
And a dynamic picture.

