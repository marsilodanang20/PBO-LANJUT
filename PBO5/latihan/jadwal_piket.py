from db import DBConnection as mydb

class jadwal_piket:
    def __init__(self):
        self.__id=None
        self.__nim=None
        self.__nama=None
        self.__kelas=None
        self.__kode_prodi=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def kelas(self):
        return self.__kelas

    @kelas.setter
    def kelas(self, value):
        self.__kelas = value

    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nim, self.__nama, self.__kelas, self.__kode_prodi)
        sql="INSERT INTO jadwal_piket (nim, nama, kelas, kode_prodi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nim, self.__nama, self.__kelas, self.__kode_prodi, id)
        sql="UPDATE jadwal_piket SET nim = %s, nama = %s, kelas=%s, kode_prodi=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nim):
        self.conn = mydb()
        val = (self.__nama, self.__kelas, self.__kode_prodi, nim)
        sql="UPDATE jadwal_piket SET nama = %s, kelas=%s, kode_prodi=%s WHERE nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM jadwal_piket WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nim):
        self.conn = mydb()
        sql="DELETE FROM jadwal_piket WHERE nim='" + str(nim) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM jadwal_piket WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nim = self.result[1]
        self.__nama = self.result[2]
        self.__kelas = self.result[3]
        self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM jadwal_piket WHERE nim='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[1]
            self.__nama = self.result[2]
            self.__kelas = self.result[3]
            self.__kode_prodi = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''
            self.__nama = ''
            self.__kelas = ''
            self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM jadwal_piket"
        self.result = self.conn.findAll(sql)
        return self.result

# delete Data
A = jadwal_piket()
B = A.getAllData()
print(B)