import ast


sum = "1/2"
tree = ast.parse(sum)

print(ast.dump(tree))

# ast.walk() is a generator
nodes = ast.walk(tree)

# for node in nodes:
  # print(node)


# There are alternatives to the ast.walk() helper
# The first is ast.NodeVisitor class.
# It scans the tree and calls a visitor function to every node

# You can use it by subclassing it and overriding visit() methods
# that should have the names of the corresponding node classes
class BinOpLister(ast.NodeVisitor):
  def visit_BinOp(self, node):
    print(node.left)
    print(node.op)
    print(node.right)
    self.generic_visit(node)

  
BinOpLister().visit(tree)


# ast.literal_eval()
user_input = "15"
print(type(user_input))

check_user_input = ast.literal_eval(user_input)  # Parses it to int
print(check_user_input, type(check_user_input))


# The ast nodes
# Each node is a construct that describes a part of the source code.
# In the ast module they are divided into classes, and most of them
# also have attributes that store the most useful information

# Example
with open('greet.py') as file:
  tree = ast.parse(file.read())

# print(ast.dump(tree))
# import_ = tree.body[0]

class ImportLister(ast.NodeVisitor):
  def visit_Import(self, node):
    print(node.names[0].name)
    

ImportLister().visit(tree)

# function = fun_tree.body[0]
# fun_args = function.args.args

# args = [arg.arg for arg in fun_args]
# print(args)


