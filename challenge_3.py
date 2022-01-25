# algorithm found here: https://gist.github.com/dishbreak/48bca2c9c60420a53920c39e08d16c56

def get_parent(height, index):
    max_index = 2**height - 1       # max num of nodes

    if max_index < index:
        return -1

    else:
        node_offset = 0                 # used for node prediction? left and right
        continue_flag = True
        subtree_size = max_index        # set subtree size
        parent = -1                     # store parent

        while continue_flag:
            if subtree_size == 0:
                # kill program
                continue_flag = False

            # Original Note: right shift is equivalent to dividing by 2 and discarding the remainder.
            # ^ bit shift?
            subtree_size = subtree_size >> 1

            # left and right node prediction
            left_node = node_offset + subtree_size
            right_node = left_node + subtree_size

            # original=my_node; current node?
            curr_node = right_node + 1

            # if either child is a match, parent = current node
            if left_node == index or right_node == index:
                parent = curr_node
                continue_flag = False

            # Original Note: Make the current left child the offset if the index is greater than the left.
            #                This effectively searches down the right subtree.
            if index > left_node:
                node_offset = left_node

        return parent

def solution(height, list):
    parents = [get_parent(height, i) for i in list]
    return parents
