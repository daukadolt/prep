### Master's Method
1. f(n) = O(n^[logb(a)-epsilon]) dominates the runtime, therefore T(n) = Theta(n^[logb(a)]). "Leaf-heavy" recursion tree
2. f(n) = Theta(n^[logb(a)]) (special case without lg(n)^k), subproblems comparable to f(n). T(n) = Theta(n^[logb(a)])
3. f(n) = BigOmega(n^[logb(a) + epsilon]). f(n) dominates the runtime, given that a(f(n/b)) <= c(f(n)), c<0. T(n) = Theta(f(n))

