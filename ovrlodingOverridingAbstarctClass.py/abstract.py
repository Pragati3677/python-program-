from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def  make_sound(self):
        pass

class dog(animal):
    def make_sound(self):
        print("dog barks")

d = dog()
d.make_sound()



