x = x*y
(x)(y)(temp0)(xtemp)(ycount)
Own work! Convoluted solution

,         		x
> +++     		y=3 (or input)

>[-]>[-]>[-] 	set cells to 0
<<<< [->>>+<<<] transfer x to xtemp
> [->+>>+<<<] 	transfer y to temp0 and ycount
> [-<+>] 		transfer temp0 to y
>>
[ 				while ycount != 0
 - 				ycount decrement
 < [-<+<<+>>>] 	transfer xtemp to x and temp0
 < [->+<] 		transfer temp0 to xtemp
 >>
]

<<<< . 			x (might overflow)
