# Operators and Expressions 
# Evaluation Order
# 
#   lambda : Lambda Expression 
#   if - else : Conditional Expression
#   or  : Boolean OR
#   and : Boolean AND
#   not x : Boolean Not
#   in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, 
#                      including membership tests and identity tests
#   | : Bitwise OR
#   ^ : Bitwise XOR
#   & : Bitwise AND
#   <<,>>: Shifts 
#   +, - : Addition and Subtraction
#   *, /, //, % : Multiplication, Division, Floor Division, and Remainder
#   +x, -x, ~x, : Postive, Negative, bitwise NOT 
#   ** : Exponentiation
#   x[index], x[index:index], x(arguments...), {key: value...}, {expressions...} : 
#   Binding or tuple display, list display, dictionary display, set display

length = 5
breadth = 2

area = length * breadth

print('Area is', area)
print('Perimeter is', 2*(length + breadth))