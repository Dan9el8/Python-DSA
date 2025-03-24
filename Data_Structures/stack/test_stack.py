class Stack:
ElementwithCachedl{ax = collections. namedtuple ('Elementl{ithCachedl.lax' ,
('element', 'max'))
def --init--(se1f):
self . _element_with_cached_max = []
def empty(self):
return len(self.-element-with-cached_max) == 0
def max(self):
if seIf. emptyO:
raise IndexError('maxO: empty stack')
return self . -element_with-cached-max [-1] . max
def pop(seIf):
if self. emptyO :
raise IndexError ('pop O : empty stack')
return self. -element-with_cached-max .pop O . element
def push (self , x) :
self . -element-with-cached-max. append (
self.ElementWithcachedllax(x, x if self.emptyO else max(
x, self.maxO)))