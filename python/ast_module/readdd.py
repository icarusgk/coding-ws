import ast

with open('greet.py', 'r') as file:
  tree = ast.parse(file.read())
  nodes = ast.walk(tree)
  for node in nodes:
    if isinstance(node, ast.FunctionDef):
      
      for variable in node.body:
        print(variable.targets[0].id)