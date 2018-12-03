import sys

def push(c:chr):
	global memoryStack
	memoryStack.append(c)

def inputChar():
	global memoryStack
	r = input()
	memoryStack.append(r[0])

def outputChar():
	global memoryStack
	print(memoryStack[-1],end="")
	memoryStack = memoryStack[:-1]

def pop():
	global memoryStack
	r =memoryStack[-1]
	memoryStack = memoryStack[0:-1]
	return r

def add():
	global memoryStack
	l = ord(memoryStack[-2])
	r = ord(memoryStack[-1])
	memoryStack = memoryStack[:-2]
	memoryStack.append(chr((l+r)%128))

def jump(i:int):
	global iptr, memoryStack
	if memoryStack[-1] == "D":
		memoryStack = memoryStack[:-1]
		iptr = i
	
def parseInt(program, iptr):
	n = ""
	while iptr < len(program) and program[iptr] in "0123456789":
			n = n+program[iptr]
			iptr+=1
	if len(n) == 0:
		return 0
	return iptr,int(n)

def parseChar(program, iptr):
	return iptr+1,program[iptr]

def step(program):
	global iptr
	instruction = instructions[program[iptr]]
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

instructions = {	"p":[chr,push],
					"i":[None,inputChar],
					"o":[None,outputChar],
					"P":[None,pop],
					"a":[None,add],
					"j":[int,jump]}


if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		program = f.read()

	memoryStack = []
	iptr = 0

	while iptr < len(program):
		step(program)

	print("\nMemory after execution: "+str(memoryStack))
