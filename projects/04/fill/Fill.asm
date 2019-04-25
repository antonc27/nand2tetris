// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(START)
	@KBD
	D=M
	@KBD_UNPRESSED
	D;JEQ

(KBD_PRESSED)
	@color
	M=-1
	@FILL_START
	0;JMP

(KBD_UNPRESSED)
	@color
	M=0

(FILL_START)

	@SCREEN
	D=A

	@i
	M=D

(FILL_LOOP)
	@i // if (i - (@KBD - 1))=0 goto FILL_END
	D=M
	@KBD // keyboard is just after screen, so we can use it as stop cond
	D=D-A
	D=D+1
	@FILL_END
	D;JGT

	@color
	D=M
	@i // Blacken current word on the screen
	A=M
	M=D

	@i // i++
	M=M+1
	@FILL_LOOP // goto FILL_LOOP
	0;JMP
(FILL_END) // start again
	@START
	0;JMP