class animal:
    def make_sound(self):
        print("some generic animal sound")
class dog(animal):
    def make_sound(self):
        print("Dog barks")

a = dog()
a.make_sound()
