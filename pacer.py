import keyboard
import os
import glob
import sys
import shutil

banner1 = r'            _   __,   __   _   ,_    ' 
banner2 = r'          |/ \_/  |  /    |/  /  |   ' 
banner3 = r'          |__/ \_/|_/\___/|__/   |_/ '
banner4 = r'         /|                          '
banner5 = r'         \|                          '
banner = [banner1,banner2,banner3,banner4,banner5]
                              
run = True
selected = 0
files = [f for f in glob.glob('*')]
message = ''
move_file = ''

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_menu():    
    global selected
    term_columns = shutil.get_terminal_size().columns
    big = term_columns > 200
    if big:
        margin = ' ' * int(term_columns/10)
    else:
        margin = ' '
    line = '-' * term_columns
    clear()
    if big:
        for b in banner:
            print((' ' * 40) + (margin * int(2)) + b)
        print(margin + 'Pacer is a console based file browser. You can explore and launch files with the arrow keys, run commands with <F5>, move files with c & p, delete with <DEL> and exit with q')
        print(line)
    else:
        print(margin + 'Pacer')
        print(margin + '- move with arrow keys')
        print(margin + '- run commands with <F5>')
        print(margin + '- exit with q')
        print(margin + '- move with c & p')
        print(margin + '- delete with <DEL>')
        print('')

    ### directory_list
    curr_f = [f + ' ' * int(40-len(f)) if len(f) < 40 else '...' + f[-37:] for f in files]
    
    prev_f = [f for f in glob.glob('../*')]
    prev_f = [f.split('\\',1)[-1] for f in prev_f]
    prev_f = [f + ' ' * int(40-len(f)) if len(f) < 40 else '...' + f[-37:] for f in prev_f]
    
    try:
        next_f = [f for f in glob.glob(files[min(max(0,selected),len(files)-1)] + '/*')]
        next_f = [f.split('\\',1)[-1] for f in next_f]
        next_f = [f + ' ' * int(40-len(f)) if len(f) < 40 else f[-37:] + '...' for f in next_f]
    except:
        next_f = []

    dynamic_size = max(10, shutil.get_terminal_size().lines - 20)

    selected = min(max(selected, 0),len(files)-1)
    file_range_trans = curr_f[max(0,selected-(dynamic_size-1)):]
    file_range = range(0,dynamic_size) 

    for i in file_range:

        # previour file
        if i >= 0 and i < len(prev_f):
            prev = prev_f[i]
        else:
            prev = ' ' * 40

        # current file
        if selected == i or (selected > dynamic_size-1 and i == dynamic_size-1):
            cursor = ' >> '
        else:
            cursor = '    '

        try:
            if i >= 0:
                curr = cursor + curr_f[i]
                curr = cursor + file_range_trans[i]
            else:
                curr = cursor + (' ' * 40)
        except:
            curr = cursor + (' ' * 40)

        # next file
        try:
            nxt = next_f[i]
        except:
            nxt = (' ' * 40)

        if big:
            print(margin + prev + margin + curr + margin + nxt)
        else:
            print(curr)

    if big:
        print('\n' + line)
    if len(os.getcwd()) > 100:
        print(margin + 'DIR: ...' + os.getcwd()[-97:])
    else:
        print(margin + 'DIR: ' + os.getcwd())
    try:
        if len(files[selected]) > 99:
            print(margin + 'FILE: ...' + files[selected][-96:])
        elif selected >= 0:
            print(margin + 'FILE: ' + files[selected])
        else:
            print(margin + 'FILE: <NA>')
    except:
        print(margin + 'FILE: <NA>')
    if big:
        print(line)


    if message != '':
        print(margin + message)

def move(num):
    global selected
    global message
    message = ''
    selected += num
    show_menu()
    

def left():
    global files
    global message
    global selected
    try:
        os.chdir('..')
        selected = 0
        message = ''
    except:
        pass
    files = [f for f in glob.glob('*')]
    show_menu()
    
def right():
    global files
    global message
    global selected
    try:
        os.chdir(files[selected])
        selected = 0
        message = ''
    except:
        try:
            launch()
        except: 
            message = ' Launch / Nav Error'
    files = [f for f in glob.glob('*')]
    show_menu()

def launch():
    global message
    message = ' locked while file open'
    show_menu()
    os.system(files[selected])
    message = ' unlocked!'
    show_menu()

def exec_int():
    global message
    message = ''
    show_menu()
    cmd = input(' Console Execute: ')
    os.system(cmd)

def quit():
    clear()
    os._exit(0)

def del_f():
    global message
    global files
    message= ''
    show_menu()
    cmd = input(' Delete ' + files[selected] + '? (Y/N) ')
    if cmd.lower() == 'y':
        try:
            os.system('del "' + files[selected] +'"')
            try:
                    os.system('rmdir "' + files[selected] + '"')
            except:
                pass
            files = [f for f in glob.glob('*')]
            show_menu()
        except Exception as e:
            print(' Deletion error (' + str(e) + ')')
    else:
        print(' (not deleted)')

def cut():
    global move_file
    move_file = os.getcwd() + '\\' + files[selected]
    print(' ' + move_file + " ready to move")

def paste():
    global files
    cmd = input(' Move ' + move_file + ' into current directory? (Y/N)')
    if cmd.lower() == 'y':
        os.system('move "' + move_file + '" "' + os.getcwd() + '\\"')
        files = [f for f in glob.glob('*')]
        show_menu()
        print(' file moved')
    else:
        print(' (not moved)')

show_menu()
keyboard.add_hotkey('down', lambda: move(1))
keyboard.add_hotkey('up', lambda: move(-1))
keyboard.add_hotkey('right', right)
keyboard.add_hotkey('left', left)
keyboard.add_hotkey('F5', exec_int)
keyboard.add_hotkey('Delete', del_f)
keyboard.add_hotkey('q', quit)
keyboard.add_hotkey('c', cut)
keyboard.add_hotkey('p', paste)
keyboard.wait()
