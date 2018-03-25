import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, filedialog
from tkinter import messagebox as mBox
import itertools, webbrowser, os, time


win=tk.Tk()
win.title("dodo v1.0~The Advanced wordlist Generator")
win.resizable(0, 0)

#quit command
def _quit():
	win.quit()
	win.destroy()
	exit()
#new window callback
def _newWindow():
    os.startfile(r"dodoGUI.py")
#dodo cli callback
def _dodoCli():
	os.startfile(r"dodo.py")
#about dodo callback
def _msgBox():
	mBox.showinfo("dodo v1.0", "dodo v1.0~The advanced wordlist generator\nCopyright © 2018 blurp_shell softwares\nwww.blurpshell.com")

#website callback
def _website():
	webbrowser.open_new(r"http://blurpshell.wordpress.com")

#dodo support callback
def _support():
        webbrowser.open_new(r"https://github.com/ebereorisi/dodoWordlistGenerator")

#Menu
menuBar = Menu(win)
win.config(menu=menuBar)

#Project menu
projectMenu = Menu(menuBar, tearoff=0)
projectMenu.add_command(label="New project window", command=_newWindow)
projectMenu.add_separator()
projectMenu.add_command(label="Import format")
projectMenu.add_separator()
projectMenu.add_command(label="Export format")
projectMenu.add_separator()
projectMenu.add_command(label="dodo CLI", command=_dodoCli)
projectMenu.add_separator()
projectMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="Project", menu=projectMenu)

#Help menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Website", command=_website)
helpMenu.add_separator()
helpMenu.add_command(label="Support project", command=_support)
helpMenu.add_separator()
helpMenu.add_command(label="dodo CLI", command=_dodoCli)
helpMenu.add_separator()
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)



#Overall app container
appContainer = ttk.LabelFrame(win)
appContainer.grid(column=0, row=0)

#character input box
charLabel = ttk.Label(appContainer, text="Input characters")
charLabel.grid(column=0, row=0)

charBox = ttk.Entry(appContainer, width=36)
charBox.grid(column=0, row=1)


#>min and max frame
minMaxFrame = ttk.LabelFrame(appContainer)
minMaxFrame.grid(column=0, row=2)

#minimum value box
minValLabel = ttk.Label(minMaxFrame, text="Set minimum value")
minValLabel.grid(column=0, row=0 )

#minvalBox = tk.IntVar()
minValBox = ttk.Entry(minMaxFrame, width=6)
minValBox.grid(column=0, row=1)

#maximum value box
maxValLabel = ttk.Label(minMaxFrame, text="Set maximum value")
maxValLabel.grid(column=1, row=0)

#maxValBox = tk.IntVar()
maxValBox = ttk.Entry(minMaxFrame, width=6)
maxValBox.grid(column=1, row=1)


#generate frame
genListLabel = ttk.LabelFrame(appContainer)
genListLabel.grid(column=0, row=3)

	
#genarete callback action
def _generate():
	f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	if f is None:
		return

	for n in range(int(minValBox.get()), int(maxValBox.get())+1):
		for xx in itertools.product(charBox.get(), repeat=n):
			yy = "".join(xx)				
			#print(yy)
			f.write(yy+"\n")
	f.close()
	mBox.showinfo("", "DONE")

#generate list
genList = ttk.Button(genListLabel, text="Generate", command=_generate)
genList.grid(column=1, row=0, padx=10)


win.mainloop()
