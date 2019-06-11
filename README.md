# Revision

### By 11.06.19
---------------
1. Coding 
	- [ ] System routines
	- [x] Implement traverse data structures
2. Algorithms
	- [x] Big-O
	- [x] Hashing
	- [ ] Handling obscenely large amounts of data
3. Sorting
	1. At least one O(nlgn) sorting algorithm
		- [x] Merge Sort
		- [x] Quicksort
	2. Common sorting functions
		1. Heapsort - inplace, unstable
		2. Quicksort - inplace, unstable
		3. Merge Sort - not inplace, stable
		4. Insertion Sort - inplace, stable
	3. When are they efficient, when not?
		1. Heapsort - when speed is of importance and there is a limited memory, like in embedded systems where merge sort may not fit memorywise.
        2. Quicksort - when speed is of importance, with no need for preserving relative item positioning and a need to avoid using additional storage space. Wins over merge sort due to locality principle in cache and avoiding O(n^2) scenario with randomized pivot choice.
        3. Merge Sort - when speed is of importance, relative positioning of equally-valued items is not important and additional space allocation is feasible.
        4. Insertion Sort - when operating on small lists of items with necessity for stable sort.
	4. What is the efficiency, complexity in terms of runtime, space used?
		1. Heapsort - O(nlgn) time complexity, O(1) space complexity
        2. Quicksort - O(nlgn) average, O(n^2) worst case time compleity, O(1) space complexity
        3. Merge Sort - O(nlgn) time complexity, O(n) space complexity
        4. Insertion Sort - O(n^2) average, O(n) best case time complexity, O(1) space complexity
	
### For later consideration
---------------------------
1. Implementation of a hashtable using only arrays in Python
2. O() of hashtables and maps in Python
3. NP-complete problems
4. Trees:
	- [ ] Trie-trees
	- [ ] n-ary trees
	1. One of the balanced binary trees:
		- [ ] Red/Black tree
		- [ ] Splay tree
		- [ ] AVL tree
5. Min/Max Heaps
	1. Application
	2. O() characteristics
	3. - [ ] Implementation (optional)

