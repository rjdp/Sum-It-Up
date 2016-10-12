def get_combiations(length, N, A):
    from itertools import product
    num_lists = list(product(*(range(1,A+1),)*length))
    def map_func(tpl):
        return int(''.join(map(str,tpl)))
    def filter_func(num):
        return sum(map(int,list(str(num)))) == N
    num_lists = list(map(map_func, num_lists))
    num_lists = list(filter(filter_func, num_lists))
    return num_lists

def get_count(N,A):
    return sum([len(get_combiations(length, N, A)) for length in range(1,N+1)])
