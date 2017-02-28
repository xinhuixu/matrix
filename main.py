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
ident(N);
print "ident(N)"
print_matrix(N)

scalar_mult(N, 2)
print "scalar_mult(N, 2)"
print_matrix(N)

matrix_mult(M, N)
print "M x N"
print_matrix(N)

add_edge(N, 100, 50, 0, 200, 200, 0)
print "add_edge(N, 100, 50, 0, 200, 200, 0)"
print_matrix(N)
add_edge(N, 300, 350, 0, 400, 500, 0)
print "add_edge(N, 300, 350, 0, 400, 500, 0)"
print_matrix(N)
add_edge(N, 300, 100, 0, 400, 300, 0)
print "add_edge(N, 300, 100, 0, 400, 300, 0)"
print_matrix(N)


draw_lines( N, screen, color )
display(screen)

def gallery():
    screen = new_screen()
    color = [ 255, 255, 255 ]
    T = new_matrix(4, 0)
    
