from abc import ABCMeta, abstractmethod
from random import randint

class Account:
	@abstractmethod
	def create_account(self):
		return 0

	@abstractmethod
	def authenticate(self):
		return 0

	@abstractmethod
	def withdraw(self):
		return 0

	@abstractmethod          
	def deposit(self):
		return 0

	@abstractmethod
	def display_balance(self):
		return 0


class SavingAccount(Account):
	def __init__(self):
		self.savingAccounts = {"11111" : ["hemil",1]}

	def createAccount(self, name, initial):
		self.accountNumber = randint(10000,99999)
		self.savingAccounts[self.accountNumber] = [name, initial]
		print ("Your account is successfully created, Your account number is {}".format(self.accountNumber))

	def authenticate(self, name, acno):
		if acno in self.savingAccounts.keys():
			if self.savingAccounts[acno][0] == name:
				print ("Authentication Successful!")
				self.accountNumber = acno
			return True
		else:
			print ("all keys >>>>>>>>>>>>>" + str(self.savingAccounts.keys()))
			print ("name you enter>>>>>>>>>" + name)
			print ("name in database>>>>>>>" + self.savingAccounts[acno][0])
			print ("Authentication failed")
			return False

	def withdraw(self, wamt):
		if wamt > self.savingAccounts[self.accountNumber][1]:
			print ("Insufficient Balance")    
		else:
			self.savingAccounts[self.accountNumber][1] -= wamt
			print ("Withdraw Successful") 
			self.displaybalance(self.accountNumber)

	def deposit(self, damt):
		self.savingAccounts[self.accountNumber][1] += damt
		print ("deposit Successful")
 		self.displaybalance(self.accountNumber)

	def displaybalance(self, acno):
		print ("Available balance: {}".format(self.savingAccounts[acno][1]))


savingAccount = SavingAccount()

while True:
	print ("Enter 1 to open an acc")
	print ("Enter 2 to acess existing account")
	print ("Enter 3 to exit")
	userChoice = int(raw_input(""))
	if userChoice == 1:
		name = raw_input("Enter your name: ")
		intial = int(raw_input("Enter Intial Deposit"))
		savingAccount.createAccount(name,intial)

	elif userChoice == 2:
		name = raw_input("Enter name: ")
		accountNumber = int(raw_input("Enter accountNumber: "))
		authenticateStatus = savingAccount.authenticate(name, accountNumber)
		if authenticateStatus is True:
			while True:
				print ("enter 1 to withdraw")
				print ("Enter 2 to deposite")
				print ("Enter 3 to displaybalance")
				print ("Enter 4 to exit")
				userChoice = int(raw_input(""))
				if userChoice == 1:
					withdrawAmount = int(raw_input("Enter withdrawAmount : "))
					savingAccount.withdraw(withdrawAmount)
				elif userChoice == 2:
					depositAmount = int(raw_input("Enter depositeAmount : "))
					savingAccount.deposit(depositAmount)
				elif userChoice == 3:
					savingAccount.displaybalance(accountNumber)
				elif userChoice == 4:
					break
		

	elif userChoice == 3:
		quit()
