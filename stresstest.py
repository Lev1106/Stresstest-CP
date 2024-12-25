import os, sys, time

command = "g++ -std=c++23 -Wall -Wextra -DLOCAL -O3 "
smart = "cf.cpp"
stupid = "ups.cpp"
generator = "gen.cpp"
testFile = "input.txt"
testsCount = 5000
stopAfterError = True
fullFeedback = True
fullFeedbackWithoutTests = False
timeLimit = 1000
maxLen = 1024

smartNoExtension = smart.split('.')[0]
stupidNoExtension = stupid.split('.')[0]
generatorNoExtension = generator.split('.')[0]

testsList = []

os.system("clear")
os.system(command + generator + " -o ./" + generatorNoExtension)
os.system(command + smart + " -o ./" + smartNoExtension)
os.system(command + stupid + " -o ./" + stupidNoExtension)

def printVerdict(verdict):
	s = "\033[1mТест " + str(test) + ": \033[3" + str(1 + (verdict == 'OK')) + "m" + verdict + "\033[0m\033[0m"
	print(s)

def printTest():
	print(open(testFile).read()[:maxLen])

def printOutputs():
	outputSmartShort = outputSmart[:maxLen]
	outputStupidShort = outputStupid[:maxLen]
	if ((outputSmart == outputStupid) != (outputSmartShort == outputStupidShort)):
		outputSmartShort = outputSmart
		outputStupidShort = outputStupid
	print("Вывод \033[4m" + smart + "\033[0m (" + str(round(timeSmart, 3)) + " мс): " + outputSmartShort)
	print("Вывод \033[4m" + stupid + "\033[0m (" + str(round(timeStupid, 3)) + " мс): " + outputStupidShort + "\n")

for test in range(1, testsCount + 1):
	os.system("./" + generatorNoExtension + " > " + testFile)

	start = time.time()
	outputSmart = os.popen("./" + smartNoExtension + " < " + testFile).read()
	timeSmart = time.time() - start
	
	start = time.time()
	outputStupid = os.popen("./" + stupidNoExtension + " < " + testFile).read()
	timeStupid = time.time() - start
	#print("\033[1mТест " + str(test) + ": \033[32mOK\033[0m\033[0m")
	
	isWA = ((outputSmart) != (outputStupid))
	isTL = (timeSmart * 1000 > timeLimit)
	
	if isWA or isTL:
		if isWA:
			printVerdict("WA")
		else:
			printVerdict("TL")
		printTest()
		printOutputs()
		if stopAfterError:
			sys.exit()
		testsList.append(test)

	elif fullFeedbackWithoutTests:
		printVerdict("OK")
		printOutputs()
	
	elif fullFeedback:
		printVerdict("OK")
		printTest()
		printOutputs()

if stopAfterError or len(testsList) == 0:
	print("\033[32mТест не найден!\033[0m")
else:
	print("Найдено " + str(len(testsList)) + "/" + str(testsCount) + " тестов: ")
	for test in testsList:
		print(test, end = " ")
