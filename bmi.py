length = input("How tall are you?")
length = float(length)

weight = input("Whats your weight?")
weight = float(weight)

if length > 100:
	length = (length/100)

def bmi(length, weight):
	bmi = (float(weight)/(float(length)+float(length)))
	bmi = round(bmi,1)
	print("If your weight is %s kg and your length is %s m, your BMI will be %s" % (weight, length, bmi))

bmi(length, weight)