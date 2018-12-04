import sys

def push(i:int):
	global memoryStack
	memoryStack.append(i)

def inputChar():
	global memoryStack
	r = input()
	memoryStack.append(ord(r[0]))

def outputChar():
	global memoryStack
	print(chr(memoryStack[-1]),end="")
	memoryStack = memoryStack[:-1]

def pop():
	global memoryStack
	r = memoryStack[-1]
	memoryStack = memoryStack[0:-1]
	return r

def add():
	global memoryStack
	l = memoryStack[-2]
	r = memoryStack[-1]
	memoryStack = memoryStack[:-2]
	memoryStack.append(l+r)

def sub():
	global memoryStack
	l = memoryStack[-2]
	r = memoryStack[-1]
	memoryStack = memoryStack[:-2]
	memoryStack.append(l-r)

def jump():
	global iptr, memoryStack
	if memoryStack[-2] == 1:
		iptr += memoryStack[-1]
		#print("jump to ",iptr,"(+",memoryStack[-1],")")
	memoryStack = memoryStack[:-2]

def duplicate(i:int):
	global memoryStack
	memoryStack.append(memoryStack[-(i+1)])

def delete(i:int):
	global memoryStack
	memoryStack.pop(len(memoryStack)-(i+1))

def equal():
	global memoryStack
	l = ord(memoryStack[-2])
	r = ord(memoryStack[-1])
	memoryStack = memoryStack[:-2]
	memoryStack.append(int(l==r))

def smaller():
	global memoryStack
	l = memoryStack[-2]
	r = memoryStack[-1]
	memoryStack = memoryStack[:-2]
	memoryStack.append(int(l<r))

def parseInt(program, iptr):
	n = ""
	while iptr < len(program) and program[iptr] in "-0123456789":
			n = n+program[iptr]
			iptr+=1
	if len(n) == 0:
		return 0, 0
	return iptr, int(n)


def parseChar(program, iptr):
	return iptr+1,program[iptr]

def step(program):
	global iptr 
	instruction = instructions[program[iptr]]
	#print(program[iptr])
	if instruction[0] == int:
		iptr += 1
		iptr, arg = parseInt(program, iptr)
		instruction[1](arg)
	elif instruction[0] == chr:
		iptr += 1
		iptr, arg = parseChar(program, iptr)
		instruction[1](arg)
	else:
		iptr +=1
		instruction[1]()

instructions = {	"p":[int,push],
					"i":[None,inputChar],
					"o":[None,outputChar],
					"P":[None,pop],
					"a":[None,add],
					"s":[None,sub],
					"j":[None,jump],
					"d":[int,duplicate],
					"D":[int,delete],
					"e":[None,equal],
					"S":[None,smaller]
				}


if __name__ == "__main__":
	memoryStack = [0] #default return address
	iptr = 0

	with open(sys.argv[1]) as f:
		program = f.read()
	if len(sys.argv) > 2:
		for i in range(2,len(sys.argv)):
			memoryStack.append(int(sys.argv[i]))


	while iptr < len(program):
		step(program)
		#print("{}: {}".format(iptr, memoryStack))
		#input()
	print("\nFinished: ptr = {}, memoryStack = {}".format(iptr, memoryStack))

