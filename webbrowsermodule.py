
import webbrowser, sys, pyperclip
# webbrowser.open('https://www.python.org') open website

# sys.argv['myProgram.py','6703','Bellare','Gardens','Drive']
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])    
else:
    address = pyperclip.paste()

webbrowser.open(f"https://www.google.com/maps/place/{address}/")