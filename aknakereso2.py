import time, os, random
from tkinter import *
# colorama.init()
os.system('mode con: cols=30 lines=2')

class aknakereso:
    def __init__(self,matrix_meret = 18, aknaszam = 50):
        self.t0 = 0
        self.t1 = 0
        self.flag_count = {}
        self.flag_counter = 0
        self.matrixmeret = matrix_meret
        self.felhasznaloi_matrix = [["*".strip() for i in range(matrix_meret)] for j in range(matrix_meret)]
        self.akna_matrix = [[int("0".strip()) for i in range(matrix_meret)] for j in range(matrix_meret)]
        self.aknaszam = aknaszam

    def __str__(self):
        pass

    def felhasznaloi_matrix_kiiratas(self):
        pass

    def veletlen_aknaelhelyezes(self):
        while True:
            aknaszam = 0
            for i in self.akna_matrix:
                for j in i:
                    if j == "A".strip():
                        aknaszam += 1
            if aknaszam == self.aknaszam:
                break
            x = random.randrange(0,self.matrixmeret)
            y = random.randrange(0,self.matrixmeret)
            self.akna_matrix[x][y] = ("A")


    def szomszedok(self,x,y):
        szomszedok = []
        for i,j in ((1,1),(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)):
            if (x + i) >= 0 and (y + j) >= 0 and (x + i) <= self.matrixmeret - 1 and (y + j) <= self.matrixmeret - 1:
                if self.akna_matrix[x+i][y+j] != "A" or "F":
                    szomszedok.append((x+i,y+j))
                else:
                    pass

        return szomszedok


    def aknaszamolas(self):
        for i in range(self.matrixmeret):
            for j in range(self.matrixmeret):
                if self.akna_matrix[i][j] == "A":
                    for n,m in ((1,1),(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)):
                        if (i + n) >= 0 and (j + m) >= 0 and (i + n) <= self.matrixmeret-1 and (j + m) <= self.matrixmeret-1:
                            if self.akna_matrix[i+n][j+m] != "A" and "F":
                                self.akna_matrix[i+n][j+m] += 1
                        else:
                            pass

    def win(self):
        # app.destroy()
        root.destroy()
        self.t1 = time.process_time()
        print(self.t1-self.t0)
        input(" idő alatt sikerült nyerned!" )
        exit(print("győzelem"))

    def lose(self):
        root.destroy()
        input("VESZÍTETTÉL")
        exit(print("Veszítettél"))


    def vege_van_e(self):
        n = 0
        for i, j in self.flag_count:
            if self.akna_matrix[i][j] == "A":
                n += 1
            else:
                n -= 1
        vancsillag = 0
        if n == self.aknaszam:
            for i in self.felhasznaloi_matrix:
                for j in i:
                    if j == "*":
                        vancsillag += 1
            if vancsillag == 0:
                self.win()
            else:
                return

    def felhasznaloi_matrix_csere(self,x,y,flag = None):
        if self.akna_matrix[x][y] =="A" and flag == None:
            self.lose()

        if flag == 1:
            if self.felhasznaloi_matrix[x][y] == "F":
                self.felhasznaloi_matrix[x][y] = "*"
                del self.flag_count[(x,y)]
                self.flag_counter -= 1
                self.vege_van_e()
            else:
                self.felhasznaloi_matrix[x][y] = "F"
                self.flag_counter += 1
                self.flag_count[(x,y)] = 1
                self.vege_van_e()
                return

        if self.akna_matrix[x][y] > 0:
            self.felhasznaloi_matrix[x][y] = self.akna_matrix[x][y]
            self.vege_van_e()
        if self.akna_matrix[x][y] == 0:
            self.felhasznaloi_matrix[x][y] = self.akna_matrix[x][y]
            for n,m in self.szomszedok(x,y):
                if self.felhasznaloi_matrix[n][m] == "*":
                    self.felhasznaloi_matrix[n][m] = self.akna_matrix[n][m]
                    self.felhasznaloi_matrix_csere(n,m)

    def adat_bekeres(self):
        self.t0 = time.process_time()
        while True:
            try:
                x = int(input("x: "))
                y = int(input("y: "))
                flag = int(input("flag: "))
                break
            except:
                print("érvénytelen karakter, próbálja újra\n"
                      "")
                continue


        if flag == 1:
            flag = 1
        else:
            flag = None
        x = self.felhasznaloi_matrix_csere(x,y,flag)
        os.system("cls")
        self.felhasznaloi_matrix_kiiratas()
        if x == 1:
            return

    def play(self):
        self.veletlen_aknaelhelyezes()
        self.aknaszamolas()
        self.felhasznaloi_matrix_kiiratas()

    def felulet_csere(self,x,y):
        if self.akna_matrix[x][y] == "A":
            self.lose()
        # if self.felhasznaloi_matrix[x][y] == "*":
        if self.akna_matrix[x][y] > 0:
            app.buttons[x][y].config(bg="green", text=self.akna_matrix[x][y], anchor=CENTER)
            self.felhasznaloi_matrix[x][y] = self.akna_matrix[x][y]
            self.vege_van_e()

        if self.akna_matrix[x][y] == 0:
            app.buttons[x][y].config(bg="green", text=self.akna_matrix[x][y], anchor=CENTER)
            self.felhasznaloi_matrix[x][y] = self.akna_matrix[x][y]
            for n,m in self.szomszedok(x,y):
                if self.felhasznaloi_matrix[n][m] == "*":
                    app.buttons[x][y].config(bg="green", text=self.akna_matrix[x][y], anchor=CENTER)
                    self.felhasznaloi_matrix[n][m] = self.akna_matrix[n][m]
                    self.felulet_csere(n,m)

    def flag_placement(self,x,y):
        if (self.felhasznaloi_matrix[x][y] == "*") or (self.felhasznaloi_matrix[x][y] == "F"):
            if self.felhasznaloi_matrix[x][y] == "F":
                self.felhasznaloi_matrix[x][y] = "*"
                # app.buttons[x][y].append(Button(self,height=2,width=4))
                app.buttons[x][y].config(text="",bg="grey",height=2,width=4)
                del self.flag_count[(x,y)]
                self.flag_counter -= 1
                self.vege_van_e()
            else:
                self.felhasznaloi_matrix[x][y] = "F"
                app.buttons[x][y].config(bg="red", text="F", anchor=CENTER)
                self.flag_counter += 1
                self.flag_count[(x,y)] = 1
                self.vege_van_e()
                return

    def middle_click(self,x,y):
        if self.felhasznaloi_matrix[x][y] >= 0:

            aknaszam = 0
            zaszloszam = 0
            for i, j in ((1, 1), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)):
                if (x + i) >= 0 and (y + j) >= 0 and (x + i) <= self.matrixmeret - 1 and (y + j) <= self.matrixmeret - 1:
                    if self.akna_matrix[x + i][y + j] == "A":
                        aknaszam += 1
                    if self.felhasznaloi_matrix[x + i][y + j] == "F":
                        zaszloszam += 1

            if aknaszam == zaszloszam:
                for i, j in ((1, 1), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)):
                    if (x + i) >= 0 and (y + j) >= 0 and (x + i) <= self.matrixmeret - 1 and (y + j) <= self.matrixmeret - 1:
                        if (self.akna_matrix[x + i][y + j] == "A" and self.felhasznaloi_matrix[x + i][y + j] != "F"):
                            self.lose()

                for i, j in ((1, 1), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)):
                    if (x + i) >= 0 and (y + j) >= 0 and (x + i) <= self.matrixmeret - 1 and (
                            y + j) <= self.matrixmeret - 1:
                        if self.felhasznaloi_matrix[x + i][y + j] == "*":
                            self.felulet_csere((x + i), (y + j))
                            self.felhasznaloi_matrix_csere((x + i), (y + j))


akna = aknakereso()
akna.play()
# akna.proba()
class first_window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_windows()

    def kezdo(self):
        root1.destroy()

    def init_windows(self):
        self.master.title("aknakereső")

        self.pack(fill=BOTH,expand=1)
        self.button_kezdo = Button(self,text="Kezdő",command=self.kezdo).place(x=int(akna.matrixmeret*35.3)/2,y=int(akna.matrixmeret*37.5)/2)

root1 = Tk()
app1 = first_window(root1)
x = int(akna.matrixmeret*35.3)
y = int(akna.matrixmeret*37.5)
root1.geometry("{0}x{1}".format(x,y))
root1.mainloop()


class Windows(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_windows()
        # self.buttons_back = [["0" for i in range(18)] for i in range(18)]

    def left(self,event,i,j):
        akna.felulet_csere(i,j)

    def middle(self,event,i,j):
        akna.middle_click(i,j)

    def right(selfe,event,i,j):
        akna.flag_placement(i,j)

    def init_windows(self):
        self.buttons = []
        self.master.title("aknakereső")
        self.pack(fill=BOTH,expand=1)

        for i in range(akna.matrixmeret):
            self.buttons.append([])
            for j in range(akna.matrixmeret):
                self.buttons[i].append(Button(self,bg="grey",height=2,width=4))
                self.buttons[i][j].bind("<Button-1>", func=lambda e, row=i, column=j:self.left(e, row, column))
                self.buttons[i][j].bind("<Button-2>",func=lambda e, row=i, column=j: self.middle(e, row, column))
                self.buttons[i][j].bind("<Button-3>", func=lambda e, row=i, column=j:self.right(e, row, column))
                # self.buttons[i][j].grid(row=i, column=j, sticky=E)

        for i in range(akna.matrixmeret):
            for j in range(akna.matrixmeret):
                self.buttons[i][j].place(x = 600/17*i,y=600/16*j)


root = Tk()
app = Windows(root)
root.geometry("{0}x{1}".format(x,y))
root.mainloop()
