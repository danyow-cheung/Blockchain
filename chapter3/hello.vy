name:public(Bytes[24])
# name:Bytes[24]
#https://docs.vyperlang.org/en/0.2.1/release-notes.html 變化

@external 
def __init__():
    self.name = "hello world"

@external 
def change_name(new_name:Bytes[24]):
    self.name = new_name

@external
def say_hello()-> Bytes[32]:
    return concat("hello",Bytes(self.name))
    