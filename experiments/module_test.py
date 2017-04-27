#coding=utf-8

print ("I am a module_test.py and my name is: "+ __name__)

def function1():
	print ("Hi, I am inside function1.")

print("Calling function1...")

if __name__ == '__main__':
	print ("Calling function1 - only if i'm __main__...")
	function1()