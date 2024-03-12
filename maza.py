import tkinter as tk
from tkinter import messagebox

class Kullanici:
    def __init__(self, kullanici_adi, sifre, ad="", soyad="", email="", adres=""):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.adres = adres
        self.sepet = []
        self.alisveris_gecmisi = []
        self.bakiye = 1000

    def sepete_ekle(self, urun):
        self.sepet.append(urun)

    def sepeti_goruntule(self):
        if self.sepet:
            sepet_icerigi = "\n".join([f"{urun}" for urun in self.sepet])
            messagebox.showinfo("Sepet İçeriği", f"Sepetinizdeki Ürünler:\n{sepet_icerigi}")
        else:
            messagebox.showinfo("Sepet İçeriği", "Sepetinizde hiç ürün bulunmamaktadır.")

    def alisveris_yapildi(self):
        self.alisveris_gecmisi.append(self.sepet)
        self.sepet = []

    def gecmisi_goruntule(self):
        if self.alisveris_gecmisi:
            gecmis_icerik = ""
            for i, alisveris in enumerate(self.alisveris_gecmisi, start=1):
                gecmis_icerik += f"Alışveriş {i}:\n"
                gecmis_icerik += "\n".join([f"{urun}" for urun in alisveris])
                gecmis_icerik += "\n\n"
            messagebox.showinfo("Alışveriş Geçmişi", gecmis_icerik)
        else:
            messagebox.showinfo("Alışveriş Geçmişi", "Henüz bir alışveriş yapılmamıştır.")

    def bakiye_kontrol(self):
        messagebox.showinfo("Bakiye", f"Kalan Bakiyeniz: {self.bakiye} TL")

    def bakiye_yukle(self, miktar):
        self.bakiye += miktar
        messagebox.showinfo("Bakiye Yükleme", f"{miktar} TL bakiye yüklendi. Yeni bakiyeniz: {self.bakiye} TL")

    def profil_goruntule(self):
        profil_bilgileri = f"Ad: {self.ad}\nSoyad: {self.soyad}\nE-posta: {self.email}\nAdres: {self.adres}"
        messagebox.showinfo("Profil Bilgileri", profil_bilgileri)

class AlisverisMerkeziUygulamasi:
    def __init__(self, master):
        self.master = master
        master.title("Alışveriş Merkezi Uygulaması")

        self.kullanici = None

        self.giris_cercevesi()

    def giris_cercevesi(self):
        self.giris_cerceve = tk.Frame(self.master)
        self.giris_cerceve.pack()

        self.kullanici_adi_etiket = tk.Label(self.giris_cerceve, text="Kullanıcı Adı:")
        self.kullanici_adi_etiket.grid(row=0, column=0)
        self.kullanici_adi_entry = tk.Entry(self.giris_cerceve)
        self.kullanici_adi_entry.grid(row=0, column=1)

        self.sifre_etiket = tk.Label(self.giris_cerceve, text="Şifre:")
        self.sifre_etiket.grid(row=1, column=0)
        self.sifre_entry = tk.Entry(self.giris_cerceve, show="*")
        self.sifre_entry.grid(row=1, column=1)

        self.ad_etiket = tk.Label(self.giris_cerceve, text="Ad:")
        self.ad_etiket.grid(row=2, column=0)
        self.ad_entry = tk.Entry(self.giris_cerceve)
        self.ad_entry.grid(row=2, column=1)

        self.soyad_etiket = tk.Label(self.giris_cerceve, text="Soyad:")
        self.soyad_etiket.grid(row=3, column=0)
        self.soyad_entry = tk.Entry(self.giris_cerceve)
        self.soyad_entry.grid(row=3, column=1)

        self.email_etiket = tk.Label(self.giris_cerceve, text="E-posta:")
        self.email_etiket.grid(row=4, column=0)
        self.email_entry = tk.Entry(self.giris_cerceve)
        self.email_entry.grid(row=4, column=1)

        self.adres_etiket = tk.Label(self.giris_cerceve, text="Adres:")
        self.adres_etiket.grid(row=5, column=0)
        self.adres_entry = tk.Entry(self.giris_cerceve)
        self.adres_entry.grid(row=5, column=1)

        self.giris_butonu = tk.Button(self.giris_cerceve, text="Giriş Yap", command=self.giris_yap)
        self.giris_butonu.grid(row=6, columnspan=2)

    def giris_yap(self):
        kullanici_adi = self.kullanici_adi_entry.get()
        sifre = self.sifre_entry.get()
        ad = self.ad_entry.get()
        soyad = self.soyad_entry.get()
        email = self.email_entry.get()
        adres = self.adres_entry.get()

        # Örnek olarak sadece bir kullanıcı oluşturuyoruz. Gerçek bir uygulamada kullanıcı veritabanından kontrol edilmelidir.
        if kullanici_adi == "admin" and sifre == "123456":
            self.kullanici = Kullanici(kullanici_adi, sifre, ad, soyad, email, adres)
            self.giris_cerceve.destroy()
            self.anasayfa_cercevesi()
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")

    def anasayfa_cercevesi(self):
        self.anasayfa_cerceve = tk.Frame(self.master)
        self.anasayfa_cerceve.pack()

        self.magaza_secim_etiket = tk.Label(self.anasayfa_cerceve, text="Mağaza Seçin:")
        self.magaza_secim_etiket.grid(row=0, column=0)
        self.magaza_secim = tk.StringVar()
        self.magaza_secim.set(None)
        self.magaza_secim.trace("w", self.magaza_secildi)
        for i, mağaza in enumerate(Magaza.magazalar):
            tk.Radiobutton(self.anasayfa_cerceve, text=mağaza["ad"], variable=self.magaza_secim, value=mağaza["ad"]).grid(row=i+1, column=0, sticky="w")

        self.sepet_butonu = tk.Button(self.anasayfa_cerceve, text="Sepetim", command=self.sepeti_goruntule)
        self.sepet_butonu.grid(row=len(Magaza.magazalar)+1, column=0)

        self.gecmis_butonu = tk.Button(self.anasayfa_cerceve, text="Alışveriş Geçmişim", command=self.alisveris_gecmisi_goruntule)
        self.gecmis_butonu.grid(row=len(Magaza.magazalar)+2, column=0)

        self.bakiye_kontrol_butonu = tk.Button(self.anasayfa_cerceve, text="Bakiye Kontrol", command=self.bakiye_kontrol)
        self.bakiye_kontrol_butonu.grid(row=len(Magaza.magazalar)+3, column=0)

        self.bakiye_yukle_etiket = tk.Label(self.anasayfa_cerceve, text="Bakiye Yükle:")
        self.bakiye_yukle_etiket.grid(row=len(Magaza.magazalar)+4, column=0)
        self.bakiye_yukle_entry = tk.Entry(self.anasayfa_cerceve)
        self.bakiye_yukle_entry.grid(row=len(Magaza.magazalar)+4, column=1)
        self.bakiye_yukle_butonu = tk.Button(self.anasayfa_cerceve, text="Yükle", command=self.bakiye_yukle)
        self.bakiye_yukle_butonu.grid(row=len(Magaza.magazalar)+4, column=2)

        self.profil_goruntule_butonu = tk.Button(self.anasayfa_cerceve, text="Profilim", command=self.profil_goruntule)
        self.profil_goruntule_butonu.grid(row=len(Magaza.magazalar)+5, column=0)

    def magaza_secildi(self, *args):
        secilen_magaza = self.magaza_secim.get()
        for mağaza in Magaza.magazalar:
            if mağaza["ad"] == secilen_magaza:
                self.master.withdraw()  # Ana pencereyi gizle
                MagazaSayfasi(mağaza, self.kullanici, self)
                break

    def sepeti_goruntule(self):
        self.kullanici.sepeti_goruntule()

    def alisveris_gecmisi_goruntule(self):
        self.kullanici.gecmisi_goruntule()

    def bakiye_kontrol(self):
        self.kullanici.bakiye_kontrol()

    def bakiye_yukle(self):
        try:
            miktar = float(self.bakiye_yukle_entry.get())
            self.kullanici.bakiye_yukle(miktar)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir miktar girin.")

    def profil_goruntule(self):
        self.kullanici.profil_goruntule()

class Magaza:
    magazalar = [
        {"ad": "Giyim Mağazası", "ürünler": {"Gömlek": {"fiyat": 50, "stok": 10}, "Pantolon": {"fiyat": 80, "stok": 5}, "Elbise": {"fiyat": 120, "stok": 8}, "Ceket": {"fiyat": 150, "stok": 3}}},
        {"ad": "Elektronik Mağazası", "ürünler": {"Telefon": {"fiyat": 2000, "stok": 15}, "Bilgisayar": {"fiyat": 4000, "stok": 10}, "Tablet": {"fiyat": 1500, "stok": 7}, "Kulaklık": {"fiyat": 100, "stok": 20}}},
        {"ad": "Süpermarket", "ürünler": {"Ekmek": {"fiyat": 3, "stok": 50}, "Süt": {"fiyat": 2, "stok": 40}, "Meyve": {"fiyat": 5, "stok": 30}, "Sebze": {"fiyat": 4, "stok": 35}}}
    ]

class MagazaSayfasi:
    def __init__(self, magaza, kullanici, ana_uygulama):
        self.magaza = magaza
        self.kullanici = kullanici
        self.ana_uygulama = ana_uygulama

        self.pencere = tk.Toplevel()  # Toplevel kullanarak yeni bir pencere oluştur
        self.pencere.title(f"{magaza['ad']}")

        self.mesaj = tk.Label(self.pencere, text=f"{magaza['ad']} Mağazasına hoş geldiniz! Lütfen bir ürün seçin:")
        self.mesaj.pack()

        self.ürün_listesi = tk.Listbox(self.pencere, selectmode=tk.MULTIPLE)
        for ürün, detaylar in magaza["ürünler"].items():
            self.ürün_listesi.insert(tk.END, f"{ürün} - {detaylar['fiyat']} TL - Stok: {detaylar['stok']}")
        self.ürün_listesi.pack()

        self.sepete_ekle_butonu = tk.Button(self.pencere, text="Sepete Ekle", command=self.sepete_ekle)
        self.sepete_ekle_butonu.pack()

        self.siparis_ver_butonu = tk.Button(self.pencere, text="Sipariş Ver", command=self.siparis_ver)
        self.siparis_ver_butonu.pack()

        self.geri_butonu = tk.Button(self.pencere, text="Geri", command=self.geri_git)
        self.geri_butonu.pack()

    def sepete_ekle(self):
        secilenler = self.ürün_listesi.curselection()
        for secilen_index in secilenler:
            secilen_ürün = list(self.magaza["ürünler"].keys())[secilen_index]
            stok_durumu = self.magaza["ürünler"][secilen_ürün]["stok"]
            if stok_durumu > 0:
                secilen_fiyat = self.magaza["ürünler"][secilen_ürün]["fiyat"]
                self.magaza["ürünler"][secilen_ürün]["stok"] -= 1
                self.kullanici.sepete_ekle(f"{secilen_ürün} - {secilen_fiyat} TL")
                print(f"{secilen_ürün} - {secilen_fiyat} TL sepete eklendi.")
            else:
                print(f"{secilen_ürün} stokta bulunmamaktadır.")

    def siparis_ver(self):
        if self.kullanici.sepet:
            toplam_tutar = sum([int(urun.split(' - ')[1].split(' TL')[0]) for urun in self.kullanici.sepet])
            if toplam_tutar <= self.kullanici.bakiye:
                self.kullanici.bakiye -= toplam_tutar
                self.kullanici.alisveris_yapildi()
                messagebox.showinfo("Sipariş Verildi", "Siparişiniz başarıyla alınmıştır!")
                self.ana_uygulama.master.deiconify()  # Ana pencereyi tekrar göster
                self.pencere.destroy()  # Pencereyi yok et
            else:
                messagebox.showerror("Hata", "Yetersiz bakiye! Lütfen bakiyenizi kontrol edin.")
        else:
            messagebox.showerror("Hata", "Sepetiniz boş. Lütfen bir ürün ekleyin!")

    def geri_git(self):
        self.pencere.destroy()  # Pencereyi yok et
        self.ana_uygulama.master.deiconify()  # Ana pencereyi tekrar göster

uygulama = tk.Tk()
uygulama.geometry("400x300")
AlisverisMerkeziUygulamasi(uygulama)
uygulama.mainloop()
