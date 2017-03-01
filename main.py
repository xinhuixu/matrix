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


#draw_lines( N, screen, color )
#display(screen)

def gallery():
    screen = new_screen()
    color = [ 0, 255, 255 ]
    bg = new_matrix(4, 4)
    for r in range(500):
        add_edge(bg, r, 0, 0, r, 500, 0)
    draw_lines( bg, screen, color )

    color = [ 168, 168, 168 ]
    grey = new_matrix(4, 4)
    for x in range(200, 400):
        add_edge(grey, x, x/4, 0, x, x/4 + 300, 0)
    draw_lines( grey, screen, color )

    color = [ 0, 0, 0 ]
    black = new_matrix(4, 4)
    for x in range(100, 200):
        add_edge(black, x, -1*x/2 + 150, 0, x, -1*x/2 + 450, 0)
    draw_lines( black, screen, color )

    color = [ 255, 255, 255 ]
    white = new_matrix(4, 4)
    for x in range(100, 300):
        add_edge(white, x, x/4 + 375, 0, x + 100, x/4 + 325, 0)
    draw_lines( white, screen, color )
    display(screen)

gallery()
