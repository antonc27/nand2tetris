// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// In order to calculate R0 * R1, we add R0 in the loop R1 times
	
	// Initilization
	@i
	M=0 // i=0

	@2
	M=0 // Init R2=0

(LOOP)
	// Step check
	@i
	D=M
	@R1
	D=D-M
	@END
	D;JGE // If (i-R1)>=0 goto END

	// Accumulating R0 value in R2
	@R2
	D=M
	@R0
	D=D+M
	@2
	M=D

	// Increment i
	@i
	M=M+1 // i=i+1
	@LOOP
	0;JMP // Goto LOOP
(END)
	@END
	0;JMP // Infinite loop