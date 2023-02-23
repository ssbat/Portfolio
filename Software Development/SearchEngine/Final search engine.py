import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
try:
    fen = Tk()
    nbocc = IntVar()
    PATHDIALOGUE = StringVar()
    keyword = StringVar()
    DirectoryPath = StringVar()
    upper = IntVar()
    suffix = IntVar()
    prefix = IntVar()
    ponct = IntVar()
    liste5=StringVar()

    # from tkinter import messagebox
    class textfile:
        listeall = []

        #@classmethod
        ##def afficher(cls):

        #  for i in cls.listeall:
         #       print(i)

        def __init__(self, path, keyword):
            self.keyword = keyword
            self.path = path
            self.keyword = keyword
            self.file = open(path, 'r+')
            self.size = self.size2()
            
            self.name()
            test2=self.nboccurence()
           # print(test2)
            self.nboccu = test2[0]
            self.liste3=test2[1]
            #print(self.liste3)
            self.nbwords = self.howmuchword()
            self.nblettre = self.howmuchletters()
            textfile.listeall.append(self)

        def howmuchletters(self):
            self.file.seek(0)
            cpt = 0
            for line in self.file:
                line.split()
                if ponct.get() == 0:
                    for j in line:
                        if j != '\n':
                            cpt += 1
                else:
                    for j in line:
                        if j.isalnum() == True:
                            cpt += 1

            return cpt

        def howmuchword(self):
            self.file.seek(0)
            cpt = 0
            for line in self.file:
                liste = line.split()
                cpt += len(liste)
            return cpt

        def size2(self):

            file_stats = os.stat(self.path)
           # print(file_stats.st_size)
            return str(file_stats.st_size) + 'B'

        def nboccurence(self):
         try:
            cpt = 0
            cpt2 = 0  # matchcase
            cpt3 = 0  # suffix
            cpt4 = 0
            liste4 = []
            for lineindice, line in enumerate(self.file):
                liste2 = line.split()
                for elt in liste2:

                    if upper.get() == 0:

                        if self.keyword.lower() != elt.lower():  # hon iza lkelme mana zeta yaeni sert bel suffix wel prefiix
                            if self.keyword.lower() in elt.lower():  # lkey mawjude bel kelme
                                c = len(self.keyword)
                                if suffix.get()==0:
                                    if self.keyword.lower()[0] != elt.lower()[0] and self.keyword.lower() == elt.lower()[
                                                                                                             -c:]:  # awal harf gher lkelme

                                        cpt3 = cpt3 + 1
                                        liste4.append(1+lineindice)
                                if prefix.get()==0:
                                    if self.keyword.lower()[-1] != elt.lower()[-1] and self.keyword.lower() == elt.lower()[:c]:
                                        cpt4 += 1
                                        liste4.append(1+lineindice)
                        if elt.upper() == self.keyword.upper():
                            cpt2 += 1
                            liste4.append(lineindice+1)

                    else:

                        if self.keyword != elt:
                            if self.keyword in elt:

                                c = len(self.keyword)
                                if suffix.get()==0:
                                    if self.keyword[0] != elt and self.keyword == elt[-c:]:  # awal harf gher lkelme
                                        cpt3 = cpt3 + 1
                                        liste4.append(lineindice+1)
                                if prefix.get()==0:
                                    if self.keyword[-1] != elt[-1] and self.keyword == elt[:c]:
                                        cpt4 += 1
                                        liste4.append(lineindice+1)
                        if elt == self.keyword:
                            cpt += 1
                            liste4.append(lineindice+1)





            liste4=str(liste4)
           # print(liste4)
            if ((cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 0 and suffix.get() == 0 and prefix.get() == 0:
                return [f"{cpt + cpt2 + cpt3 + cpt4}",liste4]
            else:
                if ((
                            cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 0 and suffix.get() == 1 and prefix.get() == 0:  # match_suffix ison
                    return [f"{cpt + cpt2 + cpt4}",liste4]
                else:
                    if ((cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 0 and suffix.get() == 0 and prefix.get() == 1:
                        return [f"{cpt + cpt2 + cpt3}",liste4]
                    else:
                        if ((
                                    cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 0 and suffix.get() == 1 and prefix.get() == 1:
                            return [f"{cpt + cpt2}",liste4]
                        else:
                            if ((
                                        cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 1 and suffix.get() == 0 and prefix.get() == 0:
                                return [f"{cpt + cpt3 + cpt4}",liste4]
                            else:
                                if ((
                                            cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 1 and suffix.get() == 1 and prefix.get() == 0:
                                    return [f"{cpt + cpt4}",liste4]
                                else:
                                    if ((
                                                cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 1 and suffix.get() == 1 and prefix.get() == 1:
                                        return [f"{cpt}",liste4]
                                    else:
                                        if ((
                                                    cpt + cpt2 + cpt3 + cpt4) != 0) and upper.get() == 1 and suffix.get() == 0 and prefix.get() == 1:
                                            return [f"{cpt + cpt3}",liste4]
                                        else:
                                            if ((cpt + cpt2 + cpt3 + cpt4) == 0):
                                                return ['0',liste4]
         except IndexError:
             from tkinter import messagebox

             messagebox.showerror("Erreur", 'Tu dois mettre un keyword!')

        def name(self):
            elt = self.path.split('\\')
          #  print(elt)
           # print(elt[-1][:-4])
            self.name = elt[-1][:-4]
            

        def openfile(self):
            os.startfile(self.path)

        def __str__(self):
            return str({self.name: (self.path, self.nboccurence())})


    def creefen2():
        global fen2
        #runtheprograme()

        fen2 = Toplevel(fen)  # creation d'une fenetre secondaire
        fen2.minsize(1200, 801)
        fen2.title("information")
        bg = PhotoImage(file="img5.png")
        label1 = Label(fen2, image=bg)
        label1.place(x=0, y=0)
        afficher()

        fen2.mainloop()


    def tri_selection_croissant_tuple(liste):
        #print('')
        #for i in liste:
         #   print(i.nboccu,'firsrt',end='\t')
        n = len(liste)
        i = 0
        while i < n - 1:
            j = i + 1
            indice_min = i
            while j < n:
               # print(liste[j].nboccu)
                if liste[j].nboccu < liste[indice_min].nboccu:
                    indice_min = j
                j += 1
            if indice_min != i:
                liste[i], liste[indice_min] = liste[indice_min], liste[i]
            i += 1
       # print('')
        #for i in liste:
         #   print(i.nboccu,'end',end='\t')
        return liste
    def runtheprograme():
        global listefiles

        command = creefen2
        if DirectoryPath.get() != '':
            b.state(['!disabled'])
        global liste
        dicto={}
        Folderpath = DirectoryPath.get()
       # print(Folderpath)
        for (root,dirs,files) in os.walk(Folderpath):
           # print(f"root:{root} dirs:{dirs} files:{files}")
            dicto[root]=files
       # print(dicto)
        listefiles = os.listdir(Folderpath)
        listefiles2=[]
        for pathdir in dicto:
            for filesname in dicto[pathdir]:
                listefiles2.append(f"{pathdir}\\{filesname}")
 
        #print(listefiles2)
        listefiles=listefiles2

      #  print(listefiles)
        dic = {}
       # print(keyword.get())
        #print(type(keyword.get()))
        for i in range(len(listefiles)):
            if listefiles[i][-3:] == 'txt':
                dic[listefiles[i][:-4]] = textfile(listefiles[i],
                                              keyword.get())

        for c, v in dic.items():
            liste.append({c: v})
       
        print(textfile.listeall)
        textfile.listeall=tri_selection_croissant_tuple(textfile.listeall)
       # print(liste)

        # print(textfile.listeall[0].howmuchletters())


    liste = []


    def afficher2():
        textfile.listeall = []
        runtheprograme()
        ttk.Label(fen2, text="nb of occurence", style='Special.TLabel').grid(column=2, row=1, pady=10)
        #print(textfile.listeall)

        
        #print(textfile.listeall)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.name,font='Times 12', foreground='blue').grid(column=0, row=i + 2, pady=10,sticky='N')
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.nboccu, foreground='blue').grid(column=2, sticky="N", row=i + 2, pady=10)
            if i == len(textfile.listeall) - 1:
                ttk.Checkbutton(fen2, text='Match Case', variable=upper, onvalue=1, offvalue=0, command=afficher).grid(
                    column=0, row=i + 3, pady=10, sticky='W')
                ttk.Checkbutton(fen2, text='Match Prefix', variable=suffix, onvalue=1, offvalue=0, command=afficher).grid(
                    column=0, row=i + 4, pady=10, sticky='W')
                ttk.Checkbutton(fen2, text='Match Suffix', variable=prefix, onvalue=1, offvalue=0, command=afficher).grid(
                    column=0, row=i + 5, pady=10, sticky='W')
                ttk.Checkbutton(fen2, text='Ignore punctuation', variable=ponct, onvalue=1, offvalue=0,
                                command=afficher).grid(column=0, row=i + 6, pady=10, sticky='W')

        ttk.Label(fen2, text="nb of words", style='Special.TLabel').grid(column=3, row=1, pady=10, padx=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.nbwords, foreground='blue').grid(column=3, sticky="N", row=i + 2, pady=10, padx=10)
        ttk.Label(fen2, text="nb of lettres", style='Special.TLabel').grid(column=4, row=1, pady=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.nblettre, foreground='blue').grid(column=4, sticky="N", row=i + 2, pady=10)
        ttk.Label(fen2, text="File Size", style='Special.TLabel').grid(column=5, row=1, pady=10, padx=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.size, foreground='blue').grid(column=5, sticky="N", row=i + 2, pady=10)
        ttk.Label(fen2, text="ligne", style='Special.TLabel').grid(column=7, row=1, pady=10, padx=10, sticky="W")
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.liste3, width=14, foreground='blue').grid(column=7, sticky="NE", row=i + 2, pady=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Button(fen2, text='open file', command=v.openfile).grid(column=8, sticky="N", row=i + 2, pady=10)



    def afficher():
        textfile.listeall = []
        runtheprograme()
        style = ttk.Style()
        style.configure('Special.TLabel',  foreground='red', padding=10)
     #   for i in textfile.listeall:
      #      print(i.nboccu,'1')
       # textfile.listeall=tri_selection_croissant_tuple(textfile.listeall)
        #f#or i in textfile.listeall:
          #  print(i.nboccu,'2')
        

        ttk.Label(fen2, text='Keyword is:', style='Special.TLabel').grid(column=0, row=0, pady=10)
        ttk.Label(fen2, textvariable=keyword, style='Special.TLabel', foreground='Blue').grid(column=1, row=0, pady=10)
        ttk.Label(fen2, text="Name", style='Special.TLabel').grid(column=0, row=1, pady=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.name,font='Times 10', foreground='blue').grid(column=0, row=i + 2, pady=10)

        ttk.Label(fen2, text="path", style='Special.TLabel').grid(column=1, row=1, pady=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.path, foreground='blue').grid(column=1, sticky="W", row=i + 2, pady=10)
        ttk.Label(fen2, text="nb of occurence", style='Special.TLabel').grid(column=2, row=1, pady=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.nboccu, foreground='blue').grid(column=2, sticky="N", row=i + 2, pady=10)
            if i == len(textfile.listeall) - 1:
                ttk.Checkbutton(fen2, text='Match Case', variable=upper, onvalue=1, offvalue=0, command=afficher2).grid(
                    column=0, row=i + 3, pady=10, sticky='W')
                ttk.Checkbutton(fen2, text='Match Prefix ', variable=suffix, onvalue=1, offvalue=0, command=afficher2).grid(
                    column=0, row=i + 4, pady=10, sticky='W')
                ttk.Checkbutton(fen2, text='Match Suffix', variable=prefix, onvalue=1, offvalue=0, command=afficher2).grid(
                    column=0, row=i + 5, pady=10, sticky='W')
                ttk.Checkbutton(fen2, text='Ignore punctuation', variable=ponct, onvalue=1, offvalue=0,
                                command=afficher2).grid(column=0, row=i + 6, pady=10, sticky='W')

        ttk.Label(fen2, text="nb of words", style='Special.TLabel').grid(column=3, row=1, pady=10, padx=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.nbwords, foreground='blue').grid(column=3, sticky="N", row=i + 2, pady=10, padx=10)
        ttk.Label(fen2, text="nb of lettres", style='Special.TLabel').grid(column=4, row=1, pady=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.nblettre, foreground='blue').grid(column=4, sticky="N", row=i + 2, pady=10)
        ttk.Label(fen2, text="File Size", style='Special.TLabel').grid(column=5, row=1, pady=10, padx=10)
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.size, foreground='blue').grid(column=5, sticky="N", row=i + 2, pady=10)
        ttk.Label(fen2, text="ligne", style='Special.TLabel').grid(column=7, row=1, pady=10, padx=10, sticky="W")
        for i, v in enumerate(textfile.listeall):
            ttk.Label(fen2, text=v.liste3, foreground='blue', width=14).grid(column=7, sticky="NE", row=i + 2, pady=10)

        for i, v in enumerate(textfile.listeall):
            ttk.Button(fen2, text='open file', command=v.openfile).grid(column=8, sticky="N", row=i + 2, pady=10)

        textfile.listeall = []

    def dialogue():
        open_file = filedialog.askdirectory()
        DirectoryPath.set(open_file)
        hihi()


    fen.title("Search Engine")
    fen.minsize(600, 400)
    bg = PhotoImage(file="img.png")
    label1 = Label(fen, image=bg)
    label1.place(x=0, y=0)
    fen2 = None
    s = ttk.Style()
    s2 = ttk.Style()
    s3 = ttk.Style()
    s.configure('Special.TLabel', font='Times 15', foreground='red', padding=10)
    s2.configure('Special.TButton', font='Helvetica 12', foreground='blue', background='red')


    def hihi():
        b.state(['!disabled'])


    ttk.Label(fen, text="WELCOME TO OUR SEARCH ENGINE", font=40, foreground='red', justify=CENTER,
              style='Special.TLabel').grid(row=0, column=1)  # .grid(column=1,row=0,sticky='N')
    ttk.Label(fen, text="Enter your Keyword", font=20, foreground='Blue').grid(row=1, column=0, pady=30, padx=10)
    ttk.Entry(fen, textvariable=keyword, font=20, width=27).grid(padx=10, sticky='W', row=1, column=1)
    ttk.Button(fen, text="Open Folder", style="Special.TButton", command=dialogue).grid(row=2, column=0)
    ttk.Entry(fen, textvariable=DirectoryPath, width=40).grid(padx=10, sticky='W', row=2,
                                                              column=1)  # ,validate="focusout",validatecommand=hihi
    b = ttk.Button(fen, text="Run The Search!", style="Special.TButton", command=creefen2, state='disabled')
    b.grid(column=1, row=4, sticky='WNES', pady=20)

    # ttk.Entry(frame2,textvariable=keyword).grid()

    # ttk.Button(frame2, text="run2hihi", command=runtheprograme).grid()
    # ttk.Button(frame2, text="run hihi", command=afficher).grid()
    # ttk.Button(frame2,text='openfile',command=dialogue).grid()

    # ttk.Button(frame2, text="open folder", command=dialogue).grid()
    # ttk.Label(frame2,textvariable=PATHDIALOGUE).grid()
    fen.mainloop()
except IndexError:
    from tkinter import messagebox

    messagebox.showerror("Title", "Message")
