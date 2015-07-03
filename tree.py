class Tree:
	def __init__(self, root):
		self.root = root

	# Traverses the tree and returns True if value exists
	def has_value(self, value):
		queue = [self.root]
		while queue:
			cur = queue.pop()
			if cur.value == value: 
				return True
			queue += cur.children
		return False


class TreeNode:
	def __init__(self, value, children):
		self.value = value
		self.children = children

	def add_child(self, value):
		child = TreeNode(value, [])
		self.children.append(child)