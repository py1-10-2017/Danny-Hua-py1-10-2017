class patient(object):
	patientid = 0
	def __init__(self, name, allergies):
		patient.patientid += 1
		self.id = patient.patientid
		self.name = name
		self.allergies = allergies
		self.bed_num = "none"

	def display_all(self):
		for att, val in self.__dict__.iteritems():
			print "{}: {}".format(att, val)
		print "==========================================="


class hospital(object):
	def __init__(self, hospital_name, capacity):
		self.patients = []
		self.hospital_name = hospital_name
		self.capacity = capacity
		self.hospital_beds = self.capacity

	def admit(self, patient):
		if len(self.patients) > self.capacity:
			print "Hospital is full"
		else:
			patient.bed_num = self.hospital_beds
			self.hospital_beds -= 1
			self.patients.append(patient)
		return self

	def discharge(self, patient_id):
		for patient in self.patients:
			if patient_id == patient.id:
				self.patients.remove(patient)
		return self

	def info(self):
		for patient in self.patients:
			patient.display_all()
			print "-----------------------------------------------"

patient1 = patient("Mario", "Mushroom")
patient2 = patient("Luigi", "Flowers")
patient3 = patient("Peach", "Blue")
patient4 = patient("Toad", "Fire")
patient5 = patient("Bowser", "Mario")

hospital1 = hospital("Small CLinic", 4)
hospital2 = hospital("Big CLinic", 5)
hospital1.admit(patient1).admit(patient2).admit(patient3).admit(patient4).admit(patient5).discharge(3).info()