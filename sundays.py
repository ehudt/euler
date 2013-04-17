import sys, os

class Calendar(object):
	months = {
		1 : 31,
		2 : 28,
		3 : 31,
		4 : 30,
		5 : 31,
		6 : 30,
		7 : 31,
		8 : 31,
		9 : 30,
		10 : 31,
		11 : 30,
		12 : 31,
	}
	def __init__(self):
		self.year = 1900
		self.month = 1
		self.day = 1
		self.weekday = 2
	def isLeap(self):
		if self.month == 2 and \
			((self.year % 4 == 0 and self.year % 100 != 0) or \
			(self.year % 100 == 0 and self.year % 400 == 0)):
			return 1
		else:
			return 0
	def incrementDay(self):
		if self.day == self.months[self.month] + self.isLeap():
			self.day = 1
			if self.month == 12:
				self.month = 1
				self.year += 1
			else:
				self.month += 1
		else:
			self.day += 1
		self.weekday = (self.weekday % 7) + 1

	def isSunday(self):
		return self.weekday == 1
	def getDayOfMonth(self):
		return self.day
	def getYear(self):
		return self.year

def main():
	cal = Calendar()
	counter = 0
	while cal.getYear() <= 2000:
		if cal.year >= 1901 and cal.isSunday() and cal.getDayOfMonth() == 1:
			counter += 1
		cal.incrementDay()
	print counter


if __name__=="__main__":
	main()


		
