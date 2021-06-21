import tkinter, webbrowser

def extrairLink():
    bruto = inputComment.get()
    link = bruto[bruto.index('{"profile":174,"width":1280,"mime":"video/mp4","fps":30,"url":"') + 63: bruto.index(',"cdn":"akamai_interconnect","quality":"720p"') - 1]
    commentsList.insert(0, link)
    inputComment.delete(0, tkinter.END)

def deletar():
    if len(commentsList.curselection()) > 0:
        commentsList.delete(commentsList.curselection()[0])

def abrirLink(*args):
    weblink = commentsList.get(commentsList.curselection()[0])
    webbrowser.open(weblink)

root = tkinter.Tk()
root.geometry('800x600+100+100')
root.wm_title('Links')

commentsFrame = tkinter.LabelFrame(root, text='Links extraídos')
commentsFrame.place(relwidth=1, relheight=0.5)

commentsList = tkinter.Listbox(commentsFrame, cursor = "hand2")
commentsList.place(relwidth=1, relheight=1)
commentsList.bind('<<ListboxSelect>>' , abrirLink)

optionsFrame = tkinter.LabelFrame(root, text='Opções')
optionsFrame.place(relwidth=1, relheight=0.5, rely=0.5)

inputCommentFrame = tkinter.LabelFrame(optionsFrame, text='String bruta')
inputCommentFrame.place(relwidth=1, relheight=0.5)

inputComment = tkinter.Entry(inputCommentFrame)
inputComment.place(relwidth=0.75, relheight=1)

btnComent = tkinter.Button(inputCommentFrame, text='Extrair link', command=extrairLink)
btnComent.place(relwidth=0.25, relheight=1, relx=0.75)

btnDelete = tkinter.Button(optionsFrame, text='Deletar', command=deletar)
btnDelete.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.6)

# start app
root.mainloop()