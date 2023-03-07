# binary-tree
binary tree, return the bottom-left most value.

To return the bottom-left most value of a binary tree, we need to do a level-order traversal of the tree, which means visiting all the nodes of the tree level by level starting from the root node.

During the traversal, we keep track of the leftmost node in each level. When we finish the traversal, the leftmost node in the last level will be the bottom-left most value of the tree.

Here's the algorithm in more detail:

Create a queue to store the nodes of the tree.
Enqueue the root node to the queue.
While the queue is not empty, do the following:
a. Get the size of the queue.
b. Traverse the nodes at the current level and update the leftmost node if needed.
c. Enqueue the children of the nodes at the current level.
Return the value of the leftmost node in the last level.
