from tkinter.messagebox import showinfo, showerror
from tkinter import *
from pypresence import Presence
from os import environ
from time import time as now


rpcgui = Tk()
rpcgui.iconbitmap(f"C:/Users/{environ['username']}/AppData/Local/Discord/app-1.0.9003/app.ico")
rpcgui.title("RPC Editor")
rpcgui.config(bg="green")

pixelVirtual = PhotoImage(width=1, height=1)
args={"bg":"green" ,"fg":"white", "activebackground":"lightgreen", "activeforeground":"black"}
btnargs={"bg":"green", "fg":"white", "activebackground":"darkgreen", "activeforeground":"lightgreen"
		, "disabledforeground":"white", "compound":"c", 'image':pixelVirtual}

def value():
	CLIENT_ID = client_entry.get()
	STATE = state_entry.get()
	DETAILS = det_entry.get()
	START = str_entry.get()
	END = end_entry.get()
	LIMAGE = Limg_entry.get()
	SIMAGE = Simg_entry.get()
	LTXT = Ltxt_entry.get()
	STXT = Stxt_entry.get()
	PSIZE = partysize_entry.get()
	PMAX = partymax_entry.get()
	B1TXT = btn1_entry.get()
	B1URL = url1_entry.get()
	B2TXT = btn2_entry.get()
	B2URL = url2_entry.get()

	if CLIENT_ID == "":
		CLIENT_ID = "935585892033265764"
	if STATE == "":
		STATE = None
	if DETAILS == "":
		DETAILS = None
	if START == "":
		START = None
	elif START == "Now":
		START = now()
	if END == "":
		END = None
	if LIMAGE == "":
		LIMAGE = None
	if SIMAGE == "":
		SIMAGE = None
	if LTXT == "":
		LTXT = None
	if STXT == "":
		STXT = None

	def calc_party():
		if PSIZE == "" or PMAX == "":
			PARTY = None
		else:
			PARTY = [int(PSIZE), int(PMAX)]
		return PARTY

	def calc_btns():
		BUTTONS = []
		URL1 = not (B1TXT == "" or B1URL == "")
		URL2 = not (B2TXT == "" or B2URL == "")
		if URL1:
			BUTTONS.append({"label":B1TXT, "url":B1URL})
		if URL2:
			BUTTONS.append({"label":B2TXT, "url":B2URL})
		if len(BUTTONS) == 0:
			BUTTONS = None
		return BUTTONS

	return {"CLIENT_ID":CLIENT_ID, "STATE":STATE, "DETAILS":DETAILS, "START":START, "END":END, "LTXT":LTXT, "STXT":STXT, "LIMAGE":LIMAGE, "SIMAGE":SIMAGE, "PARTY":calc_party(), "BUTTONS":calc_btns()}

def rpcRun():
	global RPC_handler
	try:
		RPC_handler = Presence(client_id=value()["CLIENT_ID"])
		RPC_handler.connect()
		RPC_handler.update(state=value()["STATE"], details=value()["DETAILS"], start=value()["START"], end=value()["END"],
			large_image=value()["LIMAGE"], small_image=value()["SIMAGE"], party_size=value()["PARTY"],
			buttons = value()["BUTTONS"], large_text=value()["LTXT"],small_text=value()["STXT"])
		showinfo("Rich Presence", "Rich Presence has Started.")
	except Exception as e:
		showerror("RPC Error", e)

def rpcExmpl():
	entrys = [client_entry, state_entry, det_entry, str_entry, end_entry, Limg_entry, Simg_entry, Ltxt_entry, Stxt_entry, partysize_entry, partymax_entry, btn1_entry, url1_entry, btn2_entry, url2_entry]
	for x in entrys:
		x.delete(0,END)
	client_entry.insert(0, "872466409240801341")
	state_entry.insert(0, "Viewing")
	det_entry.insert(0, "Custom RPC")
	str_entry.insert(0, str(int(now())))
	end_entry.insert(0, str(int(now())+120))
	Limg_entry.insert(0, "big_img")
	Simg_entry.insert(0, "css_bg")
	Ltxt_entry.insert(0, "Cluster Series")
	Stxt_entry.insert(0, "Busy")
	partysize_entry.insert(0, "1")
	partymax_entry.insert(0, "1")
	btn1_entry.insert(0, "Github")
	url1_entry.insert(0, "https://github.com/PVER-Programz")
	btn2_entry.insert(0, "CSs Bot")
	url2_entry.insert(0, "https://discord.com/oauth2/authorize?client_id=872466409240801341&permissions=549755813887&scope=bot")

def rpcLoad(id):
	pass

def rpcSave():
	pass

def rpcStop():
	RPC_handler.close()
	showinfo("Rich Presence", "Rich Presence has been Killed.")

rpc_menu = Menu(rpcgui)
rpc_menu.add_command(label="Run", command=rpcRun)
rpc_menu.add_command(label="Example", command=rpcExmpl)
rpc_menu.add_command(label="Stop", command=rpcStop)
rpcgui.config(menu=rpc_menu)

window_height = 800
window_width = 900
screen_width = rpcgui.winfo_screenwidth()
screen_height = rpcgui.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
rpcgui.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

client_frame = LabelFrame(rpcgui, text="Client ID", bg="Green", fg="white", padx=5, pady=5)
client_frame.pack(expand="yes")
client_entry = Entry(client_frame, font=("Verdana", 17))
client_entry.pack()


info_frame = LabelFrame(rpcgui, text="Rich Presence", bg="Green", fg="white", padx=10, pady=10)
info_frame.pack(expand="yes")

holderframe = Frame(info_frame, bg="Green", padx=8, pady=8)
holderframe.pack(expand="yes")

state_frame = LabelFrame(holderframe, text="State", bg="Green", fg="white", padx=5, pady=5)
state_frame.grid(row=1, column=1)
state_entry = Entry(state_frame, font=("Verdana", 13), width=25)
state_entry.pack()

det_frame = LabelFrame(holderframe, text="Details", bg="Green", fg="white", padx=5, pady=5)
det_frame.grid(row=2, column=1, padx=7)
det_entry = Entry(det_frame, font=("Verdana", 13), width=25)
det_entry.pack()

img_frame = LabelFrame(holderframe, text="Image", bg="Green", fg="white", padx=8, pady=8)
img_frame.grid(row=1, column=2, rowspan=2)

Limg_frame = LabelFrame(img_frame, text="Large Image", bg="Green", fg="white", padx=5, pady=5)
Limg_frame.grid(row=1, column=1)
Limg_entry = Entry(Limg_frame, font=("Verdana", 13), width=25)
Limg_entry.pack()
Ltxt_entry = Entry(Limg_frame, font=("Verdana", 13), width=25)
Ltxt_entry.pack()

Simg_frame = LabelFrame(img_frame, text="Small Image", bg="Green", fg="white", padx=5, pady=5)
Simg_frame.grid(row=2, column=1)
Simg_entry = Entry(Simg_frame, font=("Verdana", 13), width=25)
Simg_entry.pack()
Stxt_entry = Entry(Simg_frame, font=("Verdana", 13), width=25)
Stxt_entry.pack()

time_frame = LabelFrame(info_frame, text="Timer", bg="Green", fg="white", padx=8, pady=8)
time_frame.pack(expand="yes")

str_frame = LabelFrame(time_frame, text="Start", bg="Green", fg="white", padx=5, pady=5)
str_frame.grid(row=1, column=1)
str_entry = Entry(str_frame, font=("Verdana", 13), width=25)
str_entry.pack(side=LEFT)

end_frame = LabelFrame(time_frame, text="End", bg="Green", fg="white", padx=5, pady=5)
end_frame.grid(row=1, column=2)
end_entry = Entry(end_frame, font=("Verdana", 13), width=25)
end_entry.pack(side=RIGHT)

holderframe2 = Frame(info_frame, bg="Green", padx=8, pady=8)
holderframe2.pack(expand="yes")

party_frame = LabelFrame(holderframe2, text="Party", bg="Green", fg="white", padx=5, pady=5)
party_frame.grid(row=1, column=1)

partysize_frame = LabelFrame(party_frame, text="Party Size", bg="Green", fg="white", padx=5, pady=5)
partysize_frame.pack(expand=True)
partysize_entry = Entry(partysize_frame, font=("Verdana", 13), width=25)
partysize_entry.pack()

partymax_frame = LabelFrame(party_frame, text="Party Max", bg="Green", fg="white", padx=5, pady=5)
partymax_frame.pack(expand=True)
partymax_entry = Entry(partymax_frame, font=("Verdana", 13), width=25)
partymax_entry.pack()

holder3 = Frame(holderframe2, bg="Green", padx=5, pady=5)
holder3.grid(row=1, column=2)

btn1_frame = LabelFrame(holder3, text="Button 1", bg="Green", fg="white", padx=5, pady=5)
btn1_frame.pack(expand=True)
btn1_entry = Entry(btn1_frame, font=("Verdana", 13), width=25)
btn1_entry.pack()
url1_entry = Entry(btn1_frame, font=("Verdana", 13), width=25)
url1_entry.pack()

btn2_frame = LabelFrame(holder3, text="Button 2", bg="Green", fg="white", padx=5, pady=5)
btn2_frame.pack(expand=True)
btn2_entry = Entry(btn2_frame, font=("Verdana", 13), width=25)
btn2_entry.pack()
url2_entry = Entry(btn2_frame, font=("Verdana", 13), width=25)
url2_entry.pack()

finalbtn_frame = Frame(rpcgui, bg="Green", padx=5, pady=5)
finalbtn_frame.pack(expand=True)

postbtn = Button(finalbtn_frame, text="Post to Client", **btnargs, width=150, command=rpcRun, height=30)
postbtn.bind("<Enter>", lambda e: postbtn.config(background="lightgreen", foreground="black"))
postbtn.bind("<Leave>", lambda e: postbtn.config(background="green", foreground="white"))
postbtn.grid(row=1, column=1, padx=10)

stopbtn = Button(finalbtn_frame, text="Kill RPC", **btnargs, width=150, command=rpcStop, height=30)
stopbtn.bind("<Enter>", lambda e: stopbtn.config(background="lightgreen", foreground="black"))
stopbtn.bind("<Leave>", lambda e: stopbtn.config(background="green", foreground="white"))
stopbtn.grid(row=1, column=2, padx=10)

rpcgui.mainloop()