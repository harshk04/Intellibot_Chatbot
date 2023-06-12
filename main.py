from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

for files in os.listdir('english/'):
    data=open('english/'+files,'r',encoding='utf-8').readlines()
    trainer.train(data)
def botReply():
    query=qfield.get()
    answer=bot.get_response(query)
    textarea.insert(END, 'YOU: '+query +'\n')
    textarea.insert(END, 'BOT: ' +answer +'\n')
    qfield.delete(0,END)


root=Tk()

root.geometry('500x600+50+50')
root.title('IntelliBot')
root.config(bg='blue')

logo=PhotoImage(file='bot.png')
header=Label(root,image=logo)
header.pack()

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame, font=('Helvetica', 16, 'bold'),height=20, yscrollcommand =scrollbar.set, wrap='word')

textarea.pack(side=LEFT)

scrollbar.config(command=textarea.yview)

qfield=Entry(root, font=('Helvetica', 16))
qfield.pack(pady=15, padx=10, fill=X)

submitpic=PhotoImage(file='ask.png')

submit=Button(root,image=submitpic, command=botReply)
submit.pack(padx=10)

root.mainloop()

