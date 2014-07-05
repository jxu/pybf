stackoverflow /a/16837051/3163618 and my own writing

+++++ +++++				initialize counter (cell #0) to 10
[						use loop to set the next four cells to 70/100/30/10
	> +++++ ++			add 7 to cell #1
	> ++++++++++		add 10 to cell #2
	> +++				add 3 to cell #3
	> +					add 1 to cell #4
	<<<< -				decrement counter (cell #0)
]
> ++ .					print "H" (cell #1: 72)
> + .					print "e" (cell #2: 101)
+++++ ++ .				print "l" (108)
.						print "l"
+++ .					print "o" (111)
> ++ .					print " " (cell #3: 32)
<< +++++ +++++ +++++ .	print "W" (cell #1: 87)
> .						print "o" (cell #2: 111)
+++ .					print "r" (114)
----- - .				print "l" (108)
----- --- .				print "d" (100)
> + .					print "!" (cell #3: 33)
> .						print NUL