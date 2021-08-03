

def depth_of_a_tree(arr):
    """
    Space ->O(n) -> hash table
    Time ->O(n), the inner while loop executes only twice.
    :param arr:
    :return:
    """
    max_depth = -1
    visited_nodes = {}
    for ind in range(0, len(arr)):
        current_depth = 0
        if visited_nodes.get(arr[ind]):
            current_depth = visited_nodes.get(arr[ind])+1
            visited_nodes[ind] = current_depth
        else:
            check_ind = ind
            while arr[check_ind] != -1:
                current_depth += 1
                check_ind = arr[check_ind]
            visited_nodes[ind] = current_depth
        max_depth = max(max_depth, current_depth)
    return max_depth


if __name__ == "__main__":
    arr =[-1,0,1,6,6,0,0,2,7]
    print(depth_of_a_tree(arr))
