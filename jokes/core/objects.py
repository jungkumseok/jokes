#jokes objects

## Primitive super-objects
class Number():
    isNumber = True
    ifText = False
    id = None
    value = None
    
class Text():
    isNumber = False
    isText = True
    id = None
    value = None
    
class Variable():
    isNumber = False
    isText = True
    id = None
    value = None
    
## Primitive objects
class Natural(Number):
    def __init__(self, value):
        super(Natural, self).__init__()
        self.value = value

class Real(Number):
    def __init__(self, value):
        super(Real, self).__init__()
        self.value = value