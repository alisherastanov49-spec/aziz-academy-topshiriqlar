def scale_all(factor, *args):
    return [x * factor for x in args]

if __name__ == '__main__':
    factor = int(input())
    args_input = list(map(int, input().split()))
                      
    result = scale_all(factor, *args_input)
    print(*(result))