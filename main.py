from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#TEST
M = new_matrix(4, 4)
#print_matrix(M)
M = scalar_mult(M,5)
print "M"
print_matrix(M)

N = new_matrix(4, 4)
print "N"
print_matrix(N)

N = matrix_mult(M, N)
print "NxM"
print_matrix(N)

add_edge(N, 100, 100, 0, 200, 100, 0)
print_matrix(N)
draw_lines( N, screen, color )
display(screen)
