def print_params (a=1, b='строка', c=True):
    print(a, b,c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])
print()
values_list = (1 ,'hello', True)
print_params(*values_list)
values_disk ={'a':'text', 'b': False,'c':2}
print_params(**values_disk)
print()
values_list_2 = (54.32,'string')
print_params(*values_list_2)