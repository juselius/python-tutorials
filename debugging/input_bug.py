def input_example():
    a = raw_input('Enter a number: ')

    if a > 0:
        print 'Positive'
    elif a == 0:
        print 'Null'
    elif a < 0:
        print 'Negative'

input_example()