#!/usr/bin/python

import os
import glob
import sys
import shutil
import key_env

banner1 = r"    ____"
banner2 = r"   / __ \____ _________  _____"
banner3 = r"  / /_/ / __ '/ __/ _  \/  __/"
banner4 = r" / ____/ /_/ / /__   __/ /"
banner5 = r"/_/    \__~_/\___/\___/_/"


banner = [banner1,banner2,banner3,banner4,banner5]

selected = 0
selection = []
files = [f for f in glob.glob('*')]
message = ''
move_file = ''
if os.name == 'nt':
    splitter = '\\'
else:
    splitter = '/'



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_menu(refresh_files=False):
    global selected
    global files
    if refresh_files:
        files = [f for f in glob.glob('*')]
    term_columns = shutil.get_terminal_size().columns
    big = term_columns >170
    if big:
        margin = ' ' * int(term_columns/10)
    else:
        margin = ' '
    line = '-' * term_columns
    clear()
    if big:
        for b in banner:
            print(margin + b)
        print(margin + 'Pacer is a console based file browser.\n' + margin + 'Explore and launch with vim keys. s for pacer commands, a for console commands.\n' + margin + 'Select and clear selection with f and d. Exit with q')
        print(line)
    else:
        print(margin + 'Pacer')
        print(margin + '- move with vim keys')
        print(margin + '- select and clear with f and d')
        print(margin + '- pacer command with s')
        print(margin + '- run commands with a')
        print(margin + '- exit with q')
        print('')

    ### directory_list

    selected_files = [s['file'] for s in selection if s['path'] == os.getcwd()]
    curr_f = [f + ' ' * int(40-len(f)) if len(f) < 40 else '...' + f[-37:] for f in files]

    prev_sel = [s['file'] for s in selection if s['path'] == os.path.abspath(os.path.join(os.getcwd(), os.pardir))]
    prev_f = [f for f in glob.glob('../*')]
    prev_f = [f.split('\\',1)[-1] for f in prev_f]
    prev_f = [f + ' ' * int(40-len(f)) if len(f) < 40 else '...' + f[-37:] for f in prev_f]

    try:
        next_f = [f for f in glob.glob(files[min(max(0,selected),len(files)-1)] + '/*')]
        next_f = [f.split(splitter,1)[-1] for f in next_f]
        next_f = [f + ' ' * int(40-len(f)) if len(f) < 40 else f[-37:] + '...' for f in next_f]
        next_sel = [s['file'] for s in selection if s['path'] == os.getcwd() + splitter + files[min(max(0,selected),len(files)-1)]]
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
            if prev.strip() in prev_sel:
                prev = '*' + prev
            else:
                prev = ' ' + prev
        else:
            prev = ' ' * 41

        # current file
        if selected == i or (selected > dynamic_size-1 and i == dynamic_size-1):
            cursor = ' >> '
        else:
            cursor = '    '

        if i < len(files) and files[i] in selected_files:
            cursor = cursor + '*'
        else:
            cursor = cursor + ' '

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
            if nxt.strip() in next_sel:
                nxt = '*' + nxt
            else:
                nxt = ' ' + nxt
        except:
            nxt = (' ' * 41)

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
    print(margin + 'Selection: ' + str([s['file'] for s in selection]))
    if big:
        print(line)

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
    cmd = input(' Delete ' + str([s['path'] + splitter + s['file'] for s in selection]) + '? (Y/N) ')
    if cmd.lower().strip() == 'y':
        for s in selection:
            try:
                os.remove(s['path'] + splitter + s['file'])
                try:
                    shutil.rmtree(s['path'] + splitter + s['file'])
                except:
                    pass
            except Exception as e:
                print(' Deletion error (' + str(e) + ')')
        clear_selection()
    else:
        print(' Not deleted.')

def select():
    global selection
    f_dict = {'path':os.getcwd(),'file':files[selected]}
    if f_dict in selection:
        selection.remove(f_dict)
    else:
        selection.append(f_dict)
    show_menu()

def clear_selection():
    global selection
    selection = []
    show_menu(refresh_files = True)

def move_file():
    global files
    cmd = input(' Move ' + str([s['path'] + splitter + s['file'] for s in selection]) + ' into current directory? (Y/N)')
    if cmd.lower().strip() == 'y':
        try:
            for s in selection:
                shutil.move(s['path'] + splitter + s['file'], str(os.getcwd()) + splitter)
            clear_selection()
            print(' Moved.')
        except Exception as E:
            print(' Move error: ' + str(E))
    else:
        print(' Not moved.')

def exec_pacer():
    cmd = input(' Command for current selections? (move, delete): ')
    if cmd.lower().strip() == 'move':
        move_file()
    elif cmd.lower().strip() == 'delete':
        del_f()
    else:
        print(' No action taken')

key_mapping = {
    106: lambda: move(1),
    107: lambda: move(-1),
    108: right,
    104: left,
    97: exec_int,
    115: exec_pacer,
    102: select,
    100: clear_selection,
    113: quit
}

show_menu()
key_env.run_environment(key_mapping, exit_feature=False)
