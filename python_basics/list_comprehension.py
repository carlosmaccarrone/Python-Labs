

class ConcreteClass:
	def __init__(self, attribute):
		self.attribute = attribute

	def start(self):
		if self.attribute:
			return "Hello world! how you doing?"


objList = [ ConcreteClass(True), ConcreteClass(True), ConcreteClass(False), ConcreteClass(False), ConcreteClass(True) ]


filtered = [ obj.start() for obj in objList if obj.attribute == True ]


print(filtered)

