class Lass:

	#Class Variables
	noOfLass=0;
	commitStatus='S'
	bfName=''
	happinessMeter=0
	pairable=True

	#Constructor
	def __init__(self,name,attractionRating,budget,intelligence,typeOfGirl):
		self.name=name;
		self.attractionRating=attractionRating
		self.budget=budget
		self.intelligence=intelligence
		self.typeOfGirl=typeOfGirl

	#Check if a guy can be paired with a gal	
	def isPairable(self,lad):
		if(self.budget>lad.budget or self.commitStatus=='C'):
			return False
		return True
	#Check Commitment Status
	def isCommitted(self):
		return self.commitStatus
	#Alter Commitment Status
	def changeCommitment(self):
		if self.commitStatus=='S':
			self.commitStatus='C'  
