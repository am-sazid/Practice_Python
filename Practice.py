# n =2
# while n <= 128 :
#     print(n)
#     n *= 2
    
    
# def calculate_square_and_cube(number):
#     square = number ** 2
#     cube = number ** 3
#     print(square)
#     print(cube)

# # Using the function for numbers 2, 3, and 4
# calculate_square_and_cube(2)
# calculate_square_and_cube(3)
# calculate_square_and_cube(4)    
    
def compute_value(a, b):
    # Solution as follows
    c = a*a + 2*a*b + b*b
    d = a + b
    print(c)
    print(d)

t = 3
for _ in range(t):
    A, B = map(int, input().split())
    compute_value(A, B)