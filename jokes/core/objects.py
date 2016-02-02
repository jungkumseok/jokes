#jokes objects
class Joke():
    isBoolean = False
    isNumber = False
    isText = False
    isFunction = False
    isVariable = False
    id = None
    value = None

## Primitive super-objects
class Boolean(Joke):
    isBoolean = True
    
    def __init__(self, value):
        if value in [True, False]:
            self.value = value
        else:
            raise RuntimeError('Boolean should be True or False')

class Number(Joke):
    isNumber = True
    
    def __init__(self, value):
        if float(value):
            self.value = value
        else:
            raise RuntimeError('Number should be a number')
    
class Text(Joke):
    isText = True
    
    def __init__(self, value):
        if type(value) == str:
            self.value = value
        else:
            raise RuntimeError('Text should be a text')
    
class Variable(Joke):
    isVariable = True
    
    def __init__(self, value):
        if re.match(r'[a-zA-Z]\w*', value):
            self.value = value
        else:
            raise RuntimeError('Cannot name a variable using "'+value+'"')

class Function(Joke):
    isFunction = True
    
## Primitive objects
class Natural(Number):
    def __init__(self, value):
        super(Natural, self).__init__()
        self.value = value

class Real(Number):
    def __init__(self, value):
        super(Real, self).__init__()
        self.value = value
        
        
###Runtime object model
node_mapping = {
                'Boolean': Boolean,
                'Number': Number,
                'Text': Text,
                'Resource': Variable,
                }    
class Node():
    uri = None
    parent = None
    joke = None
    
    def __init__(self, uri, token=None):
        self.uri = uri
        if token and token.kind in node_mapping.keys():
            self.joke = node_mapping[token.kind](token.value)
