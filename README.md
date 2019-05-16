# Acyclic optimal path

This code uses dynamic programming to find the maximum path on a weighted acyclic graph

## How to run the code
```bash
git clone https://github.com/dmnguyen92/Acyclic-optimal-path.git
python find_max_path.py
```

## What happens when the graph is no longer acyclic

The code provided works well on acyclic graphs, but for cyclic graphs (i.e. graph with loop) the code does not work properly. Instead, it lets the user know a loop exists within the graph and returns all the vertices involved. 

Now that I manage to identify all the loop, the best solution I can think of for a cyclic graph is to simplify the problem into one of two scenario:
* If the starting point is outside the loops, collapse each loop into one single node.
* If the starting point is inside one of the loop, break one connection to open the loop and collapse all other loop into points.

I have made several attempts but did not manage to properly execute this idea.


