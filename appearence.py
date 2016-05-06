from Tkinter import *

class drumSimulator():
	def app(self):
		'''as an app,all other code will call from here,so-called"interface"?
		'''
		self.root=Tk()
		self.root.mainloop()

if __name__ == '__main__':
	ds=drumSimulator()
	ds.app()