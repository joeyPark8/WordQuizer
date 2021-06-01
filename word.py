class WordQuizer:
    wordFiles = {}
    words = {}

    def load_files(self):
        file = open('control.txt', 'r', encoding='utf-8')
        while True:
            line = file.readline()
            if not line:
                file.close()
                break
            line = line.rstrip('\n')
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            splitedLine = line.split(':')
            name = splitedLine[0]
            fileName = splitedLine[1]
            self.wordFiles[name] = fileName

    def load_words(self, name):
        file = open(self.wordFiles[name], 'r', encoding='utf-8')
        while True:
            line = file.readline()
            if not line:
                file.close()
                break
            splitedLine = line.split()
            self.words[splitedLine[0]] = '{} {}'.format(splitedLine[1], splitedLine[2])


import tkinter
import random

def onselect(event):
    global btn, value
    w = event.widget
    index = int(list(w.curselection())[0])
    value = w.get(index)
    btn.pack()

def onpress():
    global value

    def check():
        global index
        lbl_a.config(text=quiz.words[chChars[index]])

    def next():
        global index
        index += 1
        if index >= len(chChars):
            index = len(chChars)
            lbl_q.config(text='FINISH')
            return
        lbl_q.config(text=chChars[index])
        lbl_a.config(text='')

    def prev():
        global index
        index -= 1
        if index < 0:
            index = 0
            return
        lbl_q.config(text=chChars[index])
        lbl_a.config(text='')

    window = tkinter.Tk()
    window.title('Word Quiz')
    window.geometry("760x570+500+200")  # 4:3
    window.resizable(False, False)

    index = 0

    quiz = WordQuizer()
    quiz.load_words(value)
    chChars = list(quiz.words.keys())
    random.shuffle(chChars)

    lbl_q = tkinter.Label(window, text=chChars[index], font=("Arial", 60))
    lbl_q.place(x=330, y=100)

    lbl_a = tkinter.Label(window, text='', font=("Arial", 20))
    lbl_a.place(x=330, y=230)

    btn_check = tkinter.Button(window, text='check', command=check)
    btn_check.place(x=330, y=350)

    btn_next = tkinter.Button(window, text='next', command=next)
    btn_next.place(x=440, y=350)

    btn_prev = tkinter.Button(window, text='prev', command=prev)
    btn_prev.place(x=405, y=350)

    window.mainloop()

if __name__ == '__main__':
    mainPage = tkinter.Tk()
    mainPage.title('word quiz')
    mainPage.geometry("640x480+500+200")  # 4:3
    mainPage.resizable(False, False)

    value = 0

    quizer = WordQuizer()
    quizer.load_files()

    lst = tkinter.Listbox()
    index = 0
    for i in quizer.wordFiles:
        lst.insert(index, i)
        index+=1
    lst.bind('<<ListboxSelect>>', onselect)
    lst.pack()

    btn = tkinter.Button(text='start', command=onpress)

    mainPage.mainloop()


