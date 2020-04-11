def fibonacci():
    '''
    This generator appends a new Fibonacci number to its list
    every time it is called. 
    The result will be we can get the first 10 Fibonacci numbers simply
    by calling our generator 10 times. If we need to go do something
    else besides generate Fibonacci numbers for a while we can do that and then
    always just call the generator again whenever we need more Fibonacci numbers.


    '''
    numbers_list = []
    while 1:
        if(len(numbers_list) < 2):
            numbers_list.append(1)
        else:
            numbers_list.append(numbers_list[-1] + numbers_list[-2])
        yield numbers_list # change this line so it yields its list instead of 1

our_generator = fibonacci()
my_output = []

for i in range(10):
    my_output = (next(our_generator))
    
print(my_output)
