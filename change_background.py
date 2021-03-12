import ctypes
from glob import glob
from random import choice

background_folder_path = r"C:\User\Pictures\Backgrounds\*"
backgrounds = [f for f in glob(background_folder_path)]
ctypes.windll.user32.SystemParametersInfoW(20, 0, choice(backgrounds), 0)
