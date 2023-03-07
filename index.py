def find_bottom_left_value(root):
    queue = [root]
    leftmost_value = None
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == 0:
                leftmost_value = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return leftmost_value
