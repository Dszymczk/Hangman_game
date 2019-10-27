import tkinter as tk


class App(tk.Frame):
	def __init__(self, parent):
		self.word =
		HEIGHT = 40
		WIDTH = 80
		frame1 = tk.Frame(parent)
		frame1.pack(padx=10, pady=10)
		img_label = tk.Label(frame1, bg="grey", width=WIDTH, height=HEIGHT)
		img_label.pack(side="left", pady=5, padx=5)
		score_frame = tk.Frame(frame1, width=round(WIDTH/2), height=round(HEIGHT))
		score_frame.pack()
		score_label1 = tk.Label(score_frame, bg="green", height=round(HEIGHT/5), width=round(WIDTH/2))
		score_label1.pack(pady=5, padx=5)
		score_label2 = tk.Label(score_frame, bg="black", height=round(HEIGHT/4), width=round(WIDTH/2))
		score_label2.pack(pady=5, padx=5)
		score_label3 = tk.Label(score_frame, bg="red", height=round(HEIGHT/5), width=round(WIDTH/2))
		score_label3.pack(pady=5, padx=5)
		next_but = tk.Button(score_frame, height=round(HEIGHT/15), text="NEXT")
		next_but.pack(pady=1, padx=5, fill="x")
		show_but = tk.Button(score_frame, height=round(HEIGHT/15), text="SHOW LETTERS")
		show_but.pack(pady=1, padx=5, fill="x")
		reset_but = tk.Button(score_frame, height=round(HEIGHT/15), text="RESET")
		reset_but.pack(pady=1, padx=5, fill="x")
		letters_frame = tk.Label(parent, bg="pink",width=WIDTH, height=round(HEIGHT/6))
		letters_frame.pack(padx=15, pady=3, fill="x")


if __name__ == "__main__":
	root = tk.Tk()
	App(root)


	root.mainloop()

