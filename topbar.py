from Tkinter import *
MAX_DRUM_NUM=5
def create_right_pad(self):
	right_frame=Frame(self.root)
	
def create_left_pad(self):
	'''creating actual pattern editor pad
	'''
	left_frame=Frame(self.root)
	left_frame.grid(row=10,column=0,columnspan=6,sticky=W+E+N+S)
	tbicon=PhotoImage(file='images/openfile.gif')
	for i in range(0,MAX_DRUM_NUM):
		button=Button(left_frame,image=tbicon)
		button.image=tbicon
		button.grid(row=i,column=0,padx=5,pady=5)
		self.drum_entry=Entry(left_frame)
		self.drum_entry.grid(row=i,column=4,padx=7,pady=2)
def create_top_bar(self):
	top_bar_frame=Frame(self.root)
	top_bar_frame.config(height=25)
	top_bar_frame.grid(row=0,columnspan=12,rowspan=10,padx=5,pady=5)
	Label(top_bar_frame,text='Units:').grid(row=0,column=4)
	self.units=IntVar()
	self.units.set(4)
	self.bpu_widget=Spinbox(top_bar_frame,from_=1,to=10,width=5,textvariable=self.units)
	self.bpu_widget.grid(row=0,column=5)
	Label(top_bar_frame,text='BPUs:').grid(row=0,column=6)
	self.bpu=IntVar()
	self.bpu.set(4)
	self.units_widget=Spinbox(top_bar_frame,from_=1,to=8,width=5,textvariable=self.bpu)
	self.units_widget.grid(row=0,column=7)