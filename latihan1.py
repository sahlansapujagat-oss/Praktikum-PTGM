class Siswa:
    sekolah = "SMK PGRI 35 Solokanjeruk"

    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    def tampilkan_profil_siswa(self):
        print(f"--- Profil Siswa ---")
        print(f"Sekolah : {Siswa.sekolah}")
        print(f"Nama    : {self.nama}")
        print(f"NIS     : {self.nis}")
        print(f"Kelas   : {self.kelas}")
        print(f"--------------------")

siswa1 = Siswa("Budi Santoso", "2025001", "XII RPL 1")
siswa2 = Siswa("Citra Kirana", "2025002", "XI TKJ 2")

siswa1.tampilkan_profil_siswa()

siswa2.tampilkan_profil_siswa()