#Kang Sheng's algorithm homework.


##1.Sort Method Compare

###1.Environment

	Ubuntu 17.10 
	Python 3.6.4
	
###2.File: 

####/sort/convention.py

Three convention sort methods, whose time complexity is O(n^2). They are bubble sort, insert sort and select sort.

####/sort/advanced.py

Four advance sort methods, whose time complexity is O(nlgn). They are built-in sort, merge sort, heap sort and quick sort.

####/sort/main.py

Quoting convention.py and advanced.py to calculate time consumed and plot  a picture.

###3.Usage

	cd ./sort
	python3 main.py
	
###4.Output

The result include time consumed for each sort method and a picture.
	Initial numbers succeed! There are 200 numbers in total.
	Function Bubble succeeded! cost 0.00459 seconds.
	Function Insert succeeded! cost 0.00202 seconds.
	Function Select succeeded! cost 0.00153 seconds.
	Function Heap succeeded! cost 0.00124 seconds.
	Function Merge succeeded! cost 0.00073 seconds.
	Function Quick succeeded! cost 0.00037 seconds.
	Function BuiltIn succeeded! cost 4.00000 seconds.

	Initial numbers succeed! There are 400 numbers in total.
	Function Bubble succeeded! cost 0.01980 seconds.
	Function Insert succeeded! cost 0.00812 seconds.
	Function Select succeeded! cost 0.00617 seconds.
	Function Heap succeeded! cost 0.00286 seconds.
	Function Merge succeeded! cost 0.00170 seconds.
	Function Quick succeeded! cost 0.00085 seconds.
	Function BuiltIn succeeded! cost 0.00011 seconds.

	Initial numbers succeed! There are 800 numbers in total.
	Function Bubble succeeded! cost 0.07825 seconds.
	Function Insert succeeded! cost 0.03523 seconds.
	Function Select succeeded! cost 0.02583 seconds.
	Function Heap succeeded! cost 0.00637 seconds.
	Function Merge succeeded! cost 0.00376 seconds.
	Function Quick succeeded! cost 0.00191 seconds.
	Function BuiltIn succeeded! cost 0.00021 seconds.

	Initial numbers succeed! There are 1600 numbers in total.
	Function Bubble succeeded! cost 0.32836 seconds.
	Function Insert succeeded! cost 0.14554 seconds.
	Function Select succeeded! cost 0.10341 seconds.
	Function Heap succeeded! cost 0.01489 seconds.
	Function Merge succeeded! cost 0.00818 seconds.
	Function Quick succeeded! cost 0.00538 seconds.
	Function BuiltIn succeeded! cost 0.00046 seconds.

	Initial numbers succeed! There are 10000 numbers in total.
	It will take too long for basic sort method Bubble.
	It will take too long for basic sort method Insert.
	It will take too long for basic sort method Select.
	Function Heap succeeded! cost 0.11678 seconds.
	Function Merge succeeded! cost 0.06509 seconds.
	Function Quick succeeded! cost 0.03625 seconds.
	Function BuiltIn succeeded! cost 0.00327 seconds.

	Initial numbers succeed! There are 100000 numbers in total.
	It will take too long for basic sort method Bubble.
	It will take too long for basic sort method Insert.
	It will take too long for basic sort method Select.
	Function Heap succeeded! cost 1.50281 seconds.
	Function Merge succeeded! cost 0.78786 seconds.
	Function Quick succeeded! cost 0.44708 seconds.
	Function BuiltIn succeeded! cost 0.04711 seconds.
	
![Alt result](https://www.github.com/techkang/alo/blob/master/sort/result.png)
