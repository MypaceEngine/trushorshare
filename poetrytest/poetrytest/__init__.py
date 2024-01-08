import importlib

m = importlib.import_module('ex1.tests') # -> 'module'
print(m.__name__) # -> 'foo.some'
mObj=m.RAGExecuter()
mObj.init()
mObj.exec()
print(m.label)

n = importlib.import_module('ex2.tests') # -> 'module'
print(n.__name__)  # -> 'bar.some'
nObj=n.RAGExecuter()
nObj.init()
nObj.exec()
print(n.label)
print("Hello")