# Deven
Deven is a simple programming Language created for my firend Deven.

## Instructions
1. `p`: Pushes the follwoing integer onto the Stack
2. `i`: Reads a char from the console and pushes its ascii value onto the Stack. This only reads the first char. All follwoing chars are ignored.
3. `o`: prints the top element of the Stack as an ascii char
4. `P`: Pops the top element from the stack
5. `a`: Adds the top two Elements of the stack together and stores the result on the stack
6. `s`: Subtracts the top two Elements of the stack together and stores the result on the stack
7. `j`: Jumps relatively to the current position by the amount stored on top of the stack if the second top value on the stack is 1
8. `d`: Duplicates the i-th element from the stack where i is the integer following the command
9. `D`: Deletes the i-th element from the stack where i is the integer following the command
10. `e`: Checks if the top two elements are equal. If yes it pushes 1 onto the stack otherwise 0.
11. `S`: Checks if the second element from top is smaller than the top element on the stack. If yes it pushes 1 onto the stack otherwise 0.

## Subroutines
When starting a new subroutine, the stack should always have the return address relative to the routine end followed by the arguments on top of it.

## Examples
There are five examples available:
1. `python3 deven.py examples/helloworld.deven` Prints "Hello World" to the console
2. `python3 deven.py examples/add.deven` Asks for two numbers and adds them together. Result has to be between 0-9 in order to be displayed correctly
3. `python3 deven.py examples/modulo.deven 17 10` Calculates modulo (in this case 17%10) and stores the result on top of the stack
4. `python3 deven.py examples/primes.deven 111` Checks if a number (in this case 111) is prime. If yes it will put 1 on top of the stack, otherwise 0.
5. `python3 deven.py examples/primelist.deven 20` Outputs for each number in the interval [2,..,n-1] wheter it is prime and outputs "y" if it is and "n" otherwise. In this case it would check from 2 to 19 and the output would be `yynynynnnynynnnyny`
