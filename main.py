from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#TEST
M = new_matrix(4, 4)
print "M"
print_matrix(M)

N = new_matrix(4, 4)
print "N"
print_matrix(N)

scalar_add(M, 4)
print "M + 4"
print_matrix(M)

scalar_mult(M, 2)
print "2 * M"
print_matrix(M)

scalar_add(N, 1)
print "N + 1"
print_matrix(N)

matrix_mult(M, N)
print "MxN"
print_matrix(N)

add_edge(N, 10, 50, 0, 20, 60, 0)
print "add edge N"
print_matrix(N)

matrix_mult(M, N)
print "MxN"
print_matrix(N)

draw_lines( N, screen, color )
display(screen)

