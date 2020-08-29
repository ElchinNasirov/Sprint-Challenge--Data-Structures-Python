
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        # compare root node, if greator or equal go right
        if value >= self.value:
            # if no child
            if self.right == None:
                # insert
                self.right = BinarySearchTree(value)
            # else try again, continue right
            else:
                return self.right.insert(value)
        # if lesser go left
        elif value < self.value:
            # if no child
            if self.left == None:
                # insert
                self.left = BinarySearchTree(value)
            # else try again, continue left
            else:
                return self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        # look at root, if root is taget return true
        if target == self.value:
            return True
        # if value is less than node
        elif target < self.value:
            # go left
            if self.left != None:
                # return if found
                return self.left.contains(target)
        # if value is greater or equal to node
        elif target >= self.value:
            # go right
            if self.right != None:
                # return if found
                return self.right.contains(target)
        # else return false
        else:
            return False 