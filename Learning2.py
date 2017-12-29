import random
import time

n = 9
r = 0
def getanswer(answerNumber):
	if answerNumber == 1:
		return"It is certain"
	elif answerNumber == 2:
		return"It is decidedly so"
	elif answerNumber == 3:
		return"Yes"
	elif answerNumber == 4 :
		return "Reply hazard try again"	
	elif answerNumber == 5:
		return "Ask again later"
	elif answerNumber == 6:
		return "Concentrate and ask again"
	elif answerNumber == 7:
		return"My reply is no"
	elif answerNumber == 8:
		return"Outlook not so good"
	elif answerNumber == 9:
		return "YOU WIN"

while r != 9:
	
	def suffix(test):
		suffix = {
			1: 'st',
			2: 'nd',
			3: 'rd',
			11: 'th',
			12: 'th',
			13: 'th',
		}
		return suffix.get(test, "th")

	def getDigitEnding(n):
		if n == 11 or n == 12 or n == 13:
			first = int(str(n)[-1])
			second = int(str(n)[-2])
			s = "%s%s" % (second, first)
			
		else:
			s = int(str(n)[-1])
		return s
	
	r = random.randint(1, 9)
	
	digit_ending = getDigitEnding(n)
	x = suffix(digit_ending)
	print("%s%s try.."%(n,x))
	time.sleep(1.)
	fortune = getanswer(r)
	print(fortune)
	n = n + 1
	time.sleep(0.5)
	if n == 15:
		print("Sorry, you suck")
		break

	
	
