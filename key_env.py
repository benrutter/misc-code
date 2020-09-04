from msvcrt import getch

def run_environment(function_mapping, exit_feature=True):
    while True:
        key = ord(getch())
        if key == 27 and exit_feature:
            break
        elif key in function_mapping:
            function_mapping[key]()

if __name__ == '__main__':
    # running demo
    print('Demo of environment, exit will break loop, enter will print hello world')
    run_environment({13: lambda: print('hello world!')})
