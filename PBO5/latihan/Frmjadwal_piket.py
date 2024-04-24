import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, StringVar, messagebox
from jadwal_piket import jadwal_piket

class Formjadwal_piket:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='NIM:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIM.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Kelas:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtKelas = StringVar()
        CboKelas = ttk.Combobox(mainFrame, width=27, textvariable=self.txtKelas)
        CboKelas.grid(row=2, column=1, padx=5, pady=5)
        CboKelas['values'] = ('TI22A', 'TI22B', 'TI22C', 'TI22D', 'TI22E')
        CboKelas.current(0)

        Label(mainFrame, text='Kode Prodi:').grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtKodeProdi = StringVar()
        Cbo = ttk.Combobox(mainFrame, width=27, textvariable=self.txtKodeProdi) 
        Cbo.grid(row=7, column=1, padx=5, pady=5)
        Cbo['values'] = ('TIF', 'IND', 'PET')
        Cbo.current()      
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idmhs', 'nim', 'nama', 'kelas', 'kode_prodi') 

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmhs', text='ID')
        self.tree.column('idmhs', width="30")
        self.tree.heading('nim', text='NIM')
        self.tree.column('nim', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('kelas', text='Kelas')
        self.tree.column('kelas', width="30") 
        self.tree.heading('kode_prodi', text='Kode Prodi')
        self.tree.column('kode_prodi', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIM.delete(0, END)
        self.txtNIM.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")       
        self.txtKodeProdi.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = jadwal_piket()
        result = mhs.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('', END, values=student)
    
    def onCari(self, event=None):
        nim = self.txtNIM.get()
        mhs = jadwal_piket()
        res = mhs.getByNIM(nim)
        rec = mhs.affected
        if(rec > 0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mhs = jadwal_piket()
        res = mhs.getByNIM(nim)
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, mhs.nama)
        kelas = mhs.kelas
        if kelas == "B":
            self.B.select()
        elif kelas == "C":
            self.C.select()
        elif kelas == "D":
            self.D.select()
        elif kelas == "E":
            self.E.select()
        else: # Default to A if not specified
            self.A.select()
        self.txtKodeProdi.set(mhs.kode_prodi)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        nim = self.txtNIM.get()
        nama = self.txtNama.get()
        kelas = self.txtKelas.get()
        prodi = self.txtKodeProdi.get()
        
        mhs = jadwal_piket()
        mhs.nim = nim
        mhs.nama = nama
        mhs.kelas = kelas
        mhs.kode_prodi = prodi
        if(self.ditemukan == True):
            res = mhs.updateByNIM(nim)
            ket = 'Diperbarui'
        else:
            res = mhs.simpan()
            ket = 'Disimpan'
            
        rec = mhs.affected
        if(rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nim = self.txtNIM.get()
        mhs = jadwal_piket()
        mhs.nim = nim
        if(self.ditemukan == True):
            res = mhs.deleteByNIM(nim)
            rec = mhs.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Formjadwal_piket(root, "Aplikasi Data Jadwal Piket")
    root.mainloop()
