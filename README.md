<div align="center">

# 🌀 Fibonacci Algorithms in Python

### 🚀 Learn Fibonacci from Beginner to Advanced with Modern Python Techniques

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=26&duration=3500&pause=1200&color=00F7FF&center=true&vCenter=true&width=850&lines=Generator+Based+Implementation;Classic+Recursive+Approach;Decorator+Memoization;Dynamic+Programming;Algorithm+Optimization+in+Python" />

<br>

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge)

![Made With Love](https://img.shields.io/badge/Made%20With-Python-blueviolet?style=for-the-badge)

</div>

---

# 📖 About

This repository demonstrates three different implementations of the Fibonacci sequence, starting from the classic recursive solution and progressing toward optimized approaches using Generators, Decorators, and Memoization.

The goal of this project is not simply generating Fibonacci numbers, but understanding how algorithm design affects performance, memory usage, and scalability.

Whether you're learning Python or preparing for coding interviews, this repository provides practical examples of important computer science concepts.

---

# ✨ Features

- Beginner to Advanced implementations
- Infinite Fibonacci Generator
- Classic Recursive Algorithm
- Decorator-Based Memoization
- Dynamic Programming Concepts
- Performance Comparison
- Time & Space Complexity Analysis
- Clean Python Code
- Well Documented
- Educational Examples

---

# 📂 Project Structure

text
Fibonacci/

├── fib_generator.py
├── fib_recursive.py
├── fib_memoization.py
└── README.md


---

# 🚀 Implementations

## 🟢 Level 1 — Generator

File

text
fib_generator.py


Uses Python's yield keyword to generate Fibonacci numbers lazily.

### Advantages

- Infinite sequence
- Memory efficient
- Fast iteration
- Ideal for large datasets

python
from fib_generator import fibonacci

gen = fibonacci()

for _ in range(10):
    print(next(gen))


Output

text
0
1
1
2
3
5
8
13
21
34


---

## 🟡 Level 2 — Recursive

File

text
fib_recursive.py


Classic recursive implementation.

Simple.

Elegant.

Very slow.

python
print(fibonacci(10))


Output

text
55


---

## 🔴 Level 3 — Memoization

File

text
fib_memoization.py


Uses a custom decorator to cache previous calculations.

python
print(fibonacci(100))


Output

text
354224848179261915075


---

# ⚡ Performance Comparison

| Method | Time Complexity | Space Complexity | Infinite | Recommended |
|---------|----------------|-----------------|-----------|-------------|
| Generator | O(n) | O(1) | ✅ | ⭐⭐⭐⭐⭐ |
| Recursive | O(2ⁿ) | O(n) | ❌ | ⭐ |
| Memoization | O(n) | O(n) | ❌ | ⭐⭐⭐⭐⭐ |

---

# 🧠 Concepts Covered

✅ Python Generators

✅ yield

✅ Recursion

✅ Call Stack

✅ Decorated Functions

✅ Memoization

✅ Dynamic Programming

✅ Algorithm Optimization

✅ Time Complexity

✅ Space Complexity

---

# 🎯 Learning Goals

After completing this project you'll understand

- Why recursion becomes slow
- Why caching improves performance
- How decorators work
- How generators save memory
- Dynamic Programming fundamentals
- Performance optimization techniques

---

# 💻 Installation

Clone the repository

bash
git clone https://github.com/taha-king86/fibonacci.git


Move into the project

bash
cd fibonacci


Run any implementation

bash
python fib_generator.py


or

bash
python fib_recursive.py


or

bash
python fib_memoization.py


---

# 📊 Complexity Analysis

| Algorithm | Best | Average | Worst |
|------------|------|----------|--------|
| Generator | O(n) | O(n) | O(n) |
| Recursive | O(2ⁿ) | O(2ⁿ) | O(2ⁿ) |
| Memoization | O(n) | O(n) | O(n) |

---

# 📚 Why Memoization?
Without caching

text
fib(40)

↓

fib(39)

↓

fib(38)

↓

fib(37)

↓

...


The same values are calculated thousands of times.

Memoization stores previous answers and instantly returns them whenever needed.

---

# 🎓 Educational Value

This repository is perfect for developers learning

- Python
- Algorithms
- Dynamic Programming
- Interview Preparation
- Performance Optimization
- Clean Code

---

# 🛠 Requirements

- Python 3.10+
- No external libraries
- Pure Python

---

# 🤝 Contributing

Contributions are welcome.

Feel free to open an Issue or submit a Pull Request if you'd like to improve the project.

---

# ⭐ Support

If this project helped you learn something new,

please consider giving it a ⭐ on GitHub.

It helps the project reach more developers.

---

<div align="center">

# 🚀 Learn • Build • Optimize

*"The fastest algorithm is the one that avoids unnecessary work."*

Made with ❤️ using Python

</div>

# fibonacci
3 Fibonacci Python exercises: Level 1 - Generator for infinite sequences. Level 2 - Classic recursion. Level 3 - Memoization with decorators (n=100+). Covers generators, recursion, decorators, caching, and DP. Includes comments and examples. Great for learning optimization and advanced Python.
