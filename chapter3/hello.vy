name: public(bytes[24])

@public 
def __init__():
    self.name = "hello world"

@public 
def change_name(new_name:bytes[24]):
    self.name = new_name

@public
def say_hello()-> bytes[32]:
    return concat("hello",self.name)
    