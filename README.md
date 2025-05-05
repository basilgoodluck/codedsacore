# 📚 Data Structures and Algorithms in Python and JavaScript

This guide provides a comprehensive roadmap for implementing and mastering Data Structures and Algorithms (DSA) in Python and JavaScript. Each data structure and algorithm includes specific operations or methods to implement, along with their time and space complexity for performance analysis. This is designed to strengthen your programming skills, improve problem-solving, and prepare you for technical interviews or real-world applications.

---

## 🎯 Goals
- Implement core data structures and algorithms in both Python and JavaScript.
- Understand and analyze time and space complexity for each implementation.
- Practice classic problems to apply your knowledge.
- Build reusable, well-documented code with unit tests.

---

## 🧱 Core Data Structures
For each data structure, implement the specified operations and analyze their time/space complexity. Test edge cases (e.g., empty structures, single elements, duplicates).

### 1. Arrays / Lists
- **Operations to Implement:**
  - `push` / `append`: Add an element to the end (O(1)).
  - `pop`: Remove and return the last element (O(1)).
  - `shift` / `pop(0)`: Remove and return the first element (O(n)).
  - `unshift` / `insert(0)`: Add an element to the beginning (O(n)).
  - `length` / `len`: Return the number of elements (O(1)).
  - `access` / `index`: Access an element by index (O(1)).
  - `insert`: Insert an element at a specific index (O(n)).
  - `delete`: Remove an element at a specific index (O(n)).
  - `slice` / `splice`: Extract or replace a portion of the array (O(n)).
- **Complexity:**
  - Space: O(n), where n is the number of elements.
  - Time: Varies by operation (see above).
- **Notes:**
  - Python: Use lists (`[]`).
  - JavaScript: Use arrays (`[]`).
  - Test resizing behavior for dynamic arrays.

### 2. Strings
- **Operations to Implement:**
  - `concat`: Combine two strings (O(n)).
  - `substring` / `slice`: Extract a portion of the string (O(n)).
  - `length`: Return the string length (O(1)).
  - `indexOf` / `find`: Find the index of a substring (O(n*m)).
  - `replace`: Replace a substring with another (O(n)).
  - `split`: Split into an array based on a delimiter (O(n)).
  - `toUpperCase` / `toLowerCase`: Convert case (O(n)).
- **Complexity:**
  - Space: O(n), where n is the string length.
  - Time: Varies by operation (see above).
- **Notes:**
  - Strings are immutable in JavaScript and Python, so operations like `replace` create new strings.
  - Explore built-in methods vs. manual implementations.

### 3. Hash Tables (Objects / Dicts / Maps)
- **Operations to Implement:**
  - `set` / `__setitem__`: Add or update a key-value pair (O(1) average).
  - `get` / `__getitem__`: Retrieve a value by key (O(1) average).
  - `delete` / `__delitem__`: Remove a key-value pair (O(1) average).
  - `has` / `__contains__`: Check if a key exists (O(1) average).
  - `keys`: Return all keys (O(n)).
  - `values`: Return all values (O(n)).
  - `length` / `len`: Return the number of key-value pairs (O(1)).
- **Complexity:**
  - Space: O(n), where n is the number of key-value pairs.
  - Time: O(1) average for most operations, O(n) worst-case due to collisions.
- **Notes:**
  - Python: Use dictionaries (`{}`).
  - JavaScript: Use `Map` or plain objects (`{}`).
  - Implement a basic hash table with collision handling (e.g., chaining).

### 4. Sets
- **Operations to Implement:**
  - `add`: Add an element (O(1) average).
  - `remove`: Remove an element (O(1) average).
  - `has` / `__contains__`: Check if an element exists (O(1) average).
  - `union`: Combine two sets (O(n+m)).
  - `intersection`: Find common elements (O(min(n,m))).
  - `difference`: Find elements in one set but not another (O(n)).
  - `size` / `len`: Return the number of elements (O(1)).
- **Complexity:**
  - Space: O(n), where n is the number of elements.
  - Time: O(1) average for most operations, O(n) for set operations.
- **Notes:**
  - Python: Use `set`.
  - JavaScript: Use `Set`.
  - Test uniqueness enforcement and hash-based operations.

### 5. Linked Lists
- **Singly Linked List Operations:**
  - `append`: Add a node to the end (O(n)).
  - `prepend`: Add a node to the beginning (O(1)).
  - `delete`: Remove a node by value or index (O(n)).
  - `find`: Search for a node by value (O(n)).
  - `reverse`: Reverse the list (O(n)).
  - `length`: Return the number of nodes (O(n) or O(1) if cached).
- **Doubly Linked List Operations:**
  - Same as above, plus:
  - `delete`: Remove a node (O(n) for search, O(1) if node is known).
  - `traverseBackward`: Traverse from tail to head (O(n)).
- **Complexity:**
  - Space: O(n), where n is the number of nodes.
  - Time: Varies by operation (see above).
- **Notes:**
  - Implement node classes/structs with `value`, `next` (and `prev` for doubly).
  - Test edge cases (empty list, single node).

### 6. Stacks
- **Operations to Implement:**
  - `push`: Add an element to the top (O(1)).
  - `pop`: Remove and return the top element (O(1)).
  - `peek`: View the top element (O(1)).
  - `isEmpty`: Check if the stack is empty (O(1)).
  - `size` / `len`: Return the number of elements (O(1)).
- **Complexity:**
  - Space: O(n), where n is the number of elements.
  - Time: O(1) for all operations.
- **Notes:**
  - Use arrays or linked lists for implementation.
  - Test LIFO (Last In, First Out) behavior.

### 7. Queues
- **Standard Queue Operations:**
  - `enqueue`: Add an element to the rear (O(1)).
  - `dequeue`: Remove and return the front element (O(1)).
  - `peek`: View the front element (O(1)).
  - `isEmpty`: Check if the queue is empty (O(1)).
  - `size` / `len`: Return the number of elements (O(1)).
- **Circular Queue Operations:**
  - Same as above, with fixed-size array wrapping.
- **Priority Queue Operations:**
  - `enqueue`: Add an element with priority (O(log n) with heap).
  - `dequeue`: Remove and return the highest-priority element (O(log n)).
- **Complexity:**
  - Space: O(n), where n is the number of elements.
  - Time: O(1) for standard/circular, O(log n) for priority queue with heap.
- **Notes:**
  - Use arrays, linked lists, or heaps as needed.
  - Test FIFO (First In, First Out) behavior.

### 8. Trees
- **Binary Tree Operations:**
  - `insert`: Add a node (O(n)).
  - `delete`: Remove a node (O(n)).
  - `search`: Find a node by value (O(n)).
  - `traverse`: Pre-order, in-order, post-order (O(n)).
- **Binary Search Tree (BST) Operations:**
  - Same as above, but:
  - `insert`: O(log n) average, O(n) worst.
  - `delete`: O(log n) average, O(n) worst.
  - `search`: O(log n) average, O(n) worst.
- **Trie (Prefix Tree) Operations:**
  - `insert`: Add a word (O(m), where m is word length).
  - `search`: Check if a word exists (O(m)).
  - `startsWith`: Check if a prefix exists (O(m)).
- **Complexity:**
  - Space: O(n), where n is the number of nodes.
  - Time: Varies by operation and tree type.
- **Notes:**
  - Implement node classes with `value`, `left`, `right` (and `children` for Trie).
  - Optionally explore self-balancing trees (AVL, Red-Black).

### 9. Heaps
- **Operations to Implement:**
  - `insert`: Add an element (O(log n)).
  - `extractMin` / `extractMax`: Remove and return the min/max element (O(log n)).
  - `peek`: View the min/max element (O(1)).
  - `size` / `len`: Return the number of elements (O(1)).
- **Complexity:**
  - Space: O(n), where n is the number of elements.
  - Time: O(log n) for insert/extract, O(1) for peek.
- **Notes:**
  - Implement as binary heaps (min or max).
  - Use arrays for storage, maintaining heap property.

### 10. Graphs
- **Adjacency List Operations:**
  - `addVertex`: Add a node (O(1)).
  - `addEdge`: Add an edge (O(1)).
  - `removeVertex`: Remove a node (O(V+E)).
  - `removeEdge`: Remove an edge (O(1)).
- **Adjacency Matrix Operations:**
  - Same as above, but:
  - `addEdge`: O(1).
  - `removeEdge`: O(1).
- **Complexity:**
  - Space: O(V+E) for adjacency list, O(V²) for matrix.
  - Time: Varies by operation.
- **Notes:**
  - Support directed and undirected graphs.
  - Test weighted vs. unweighted edges.

### 11. Union-Find (Disjoint Set)
- **Operations to Implement:**
  - `makeSet`: Create a new set (O(1)).
  - `find`: Find the root of an element (O(α(n)) amortized with path compression).
  - `union`: Merge two sets (O(α(n)) amortized).
  - `connected`: Check if two elements are in the same set (O(α(n))).
- **Complexity:**
  - Space: O(n), where n is the number of elements.
  - Time: Near O(1) with optimizations (path compression, union by rank).
- **Notes:**
  - Implement path compression and union by rank for efficiency.

---

## 🔁 Algorithm Patterns
Implement these techniques and apply them to problems. Analyze complexity for each.

- **Two Pointers:** O(n) time, O(1) space (e.g., reverse array, remove duplicates).
- **Sliding Window:** O(n) time, O(k) space (e.g., max sum subarray of size k).
- **Fast & Slow Pointers:** O(n) time, O(1) space (e.g., detect cycle in linked list).
- **Binary Search:** O(log n) time, O(1) space (e.g., search sorted array).
- **Prefix Sum:** O(n) time, O(n) space (e.g., range sum queries).
- **Recursion & Backtracking:** Varies (e.g., permutations, N-Queens).
- **Divide and Conquer:** Varies (e.g., merge sort, quicksort).
- **Greedy Algorithms:** Varies (e.g., activity selection).
- **Dynamic Programming:**
  - Memoization: O(n) space for recursive calls.
  - Tabulation: O(n) space for table.
  - Examples: Fibonacci, knapsack.
- **Bit Manipulation:** O(1) space, varies (e.g., count set bits).

---

## 🔍 Searching & Sorting
Implement and compare these algorithms.

- **Linear Search:** O(n) time, O(1) space.
- **Binary Search:** O(log n) time, O(1) space.
- **Bubble Sort:** O(n²) time, O(1) space.
- **Selection Sort:** O(n²) time, O(1) space.
- **Insertion Sort:** O(n²) time, O(1) space.
- **Merge Sort:** O(n log n) time, O(n) space.
- **Quick Sort:** O(n log n) average time, O(log n) space.
- **Counting Sort / Radix Sort:** O(n+k) time, O(n+k) space (non-comparison-based).

---

## 🌐 Graph Algorithms
Implement these for both adjacency list and matrix representations.

- **Depth-First Search (DFS):** O(V+E) time, O(V) space.
- **Breadth-First Search (BFS):** O(V+E) time, O(V) space.
- **Dijkstra’s Algorithm:** O((V+E) log V) time with priority queue, O(V) space.
- **A* Search:** Similar to Dijkstra’s, heuristic-based.
- **Topological Sort:** O(V+E) time, O(V) space.
- **Bellman-Ford:** O(V*E) time, O(V) space.
- **Floyd-Warshall:** O(V³) time, O(V²) space.
- **Union-Find:** O(α(n)) per operation with optimizations.

---

## 📚 Classic Problems
Solve these to apply your DSA knowledge. Implement in both languages.

- **Anagrams / Palindromes:** O(n) time, O(n) space.
- **Valid Parentheses:** O(n) time, O(n) space.
- **LRU Cache:** O(1) time for get/put, O(n) space.
- **N-Queens:** O(n!) time, O(n²) space.
- **Sudoku Solver:** O(9^m) time, O(1) space (m = empty cells).
- **Word Ladder:** O(N*26*L) time, O(N) space (N = word list size, L = word length).
- **Longest Substring Without Repeating Characters:** O(n) time, O(k) space.
- **Subarray Sum Equals K:** O(n) time, O(n) space.
- **Longest Common Subsequence:** O(m*n) time, O(m*n) space.
- **Knapsack Problem:** O(n*W) time, O(n*W) space.
- **Edit Distance:** O(m*n) time, O(m*n) space.
- **Median of Two Sorted Arrays:** O(log(min(m,n))) time, O(1) space.

---

## 🚀 Bonus Topics
Enhance your skills with these advanced implementations.

- **JSON Parser:** Parse a JSON string into a data structure.
- **Promise (JS):** Implement a basic Promise with `then` and `catch`.
- **Event Emitter:** Create a pub-sub system for events.
- **Debounce / Throttle:** Limit function execution rate.
- **Call, Apply, Bind (JS):** Implement function context manipulation.
- **Asynchronous Patterns:**
  - JavaScript: Use `async/await`, Promises.
  - Python: Use `asyncio` with `async def` and `await`.
- **Functional Programming:**
  - Implement `map`, `reduce`, `filter` manually.
  - Explore pure functions and immutability.

---

## 🧪 Testing
- Write unit tests for each implementation:
  - Python: Use `unittest` or `pytest`.
  - JavaScript: Use `Jest` or `Mocha`.
- Test edge cases (e.g., empty inputs, large datasets, invalid inputs).
- Validate time complexity with performance tests (e.g., measure runtime for increasing input sizes).

---

## 💡 Tips for Learning
1. **Start Small:** Begin with arrays and simple algorithms like linear search.
2. **Analyze Complexity:** Calculate Big-O for time and space for every implementation.
3. **Implement Twice:** Code in Python and JavaScript to compare language differences (e.g., Python’s dynamic lists vs. JavaScript’s arrays).
4. **Solve Problems:** Apply each data structure/algorithm to at least one classic problem.
5. **Document Code:** Add comments explaining logic and complexity.
6. **Optimize:** Revisit implementations to improve performance (e.g., use path compression in Union-Find).
7. **Track Progress:** Check off each data structure, algorithm, and problem as you complete them.

---

## 📝 Example Implementation Plan
For **Arrays**:
1. Python:
   - Implement `append`, `pop`, `insert`, etc., using lists.
   - Write tests for edge cases (empty list, single element).
   - Measure time complexity with large arrays.
2. JavaScript:
   - Implement `push`, `pop`, `splice`, etc., using arrays.
   - Test with Jest for correctness.
   - Compare with Python (e.g., array resizing behavior).
3. Problems:
   - Solve “Remove Duplicates from Sorted Array” using two pointers.
   - Analyze time/space complexity.

Repeat for each data structure and algorithm.

---

This roadmap will build a strong foundation in DSA, improve your coding fluency in Python and JavaScript, and prepare you for advanced problem-solving. Happy coding! 🚀