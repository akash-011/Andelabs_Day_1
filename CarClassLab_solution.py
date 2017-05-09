class Car(object):
	def __init__(self, name='General', model='GM', type=None):
		self.name  = name
		self.model = model
		self.type  = type
		self.speed = 0

		if self.name == 'Porshe' or self.name =='Koenigsegg':
			self.doors = 2
		else:
			self.doors = 4

		if self.type == 'trailer':
			self.wheels = 8
		else:
			self.wheels = 4
		
	def is_saloon(self):
		if self.type == 'trailer':
			return False
		else:
			return True

	def drive(self, speed):
		if speed == 7:
			self.speed = 77  
		elif speed == 3:
			self.speed = 1000
