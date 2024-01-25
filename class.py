from classConstants import CLASSES
class Class:
    def __init__(self, name, level=1):
        self.generate_class_info(name)
        self.level = level
        


    def generate_class_info(self, name):
        self.class_info = CLASSES[name]