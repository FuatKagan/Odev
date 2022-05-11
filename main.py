#Hangi Mesleğe Yatkınsın?
#Daha rahat gözükmesi için satırlar halinde yaptım

import time

#3 Seçenek olacak ve 1. sayısal, 2. sözel ve 3. sosyal puan katacak
##Bölümler Soru-cevap listeleri:
b_soru_list = ["Matematiğinize mi güvenirsiniz yoksa tarihinize mi? ", "Hayat nasıl? ",
"İnsanlarla mı konuşursunuz hayvanlarla mı? ", "Tek kişilik bir meslek mi seçersiniz yoksa takım çalışması mı? ",
"Sizce fizik mi zor yoksa edebiyat mı? ", "Diksiyonunuz iyi midir? ", "Can we continue in English? ", "Sizce tüm insanlar eşit midir? ",
"Bir matematik problemini mi yoksa bir paragraf sorusunu mu çözmeyi isterdiniz? ", "Pi sayısının ilk 3 basamağını bilir misiniz? "]
b_sayisal_cevap_list = ["matematik", "kötü", "hiç", "tek", "edebiyat", "hayır", "yes", "evet", "matematik", "evet"]
b_sozel_cevap_list = ["tarih", "hiç","hayvanlar", "fark etmez", "fizik", "evet", "absolutely", "kesinlikle", "paragraf", "asla"]
b_sosyal_cevap_list = ["hiç", "güzel", "insanlar", "takım", "hepsi", "kesinlikle", "yes", "evet", "hiç", "hayır"]


##Meslekler Sorular-Cevaplar:
#Boş olacakları "-" ile gösterdim

m_sosyal_soru_list = ["İnsanları yönetmeyi sever misin? ", "Başka insanların dertlerini dinlemekten hoşlanır mısın? ",
"Siyasetten hoşlanır mısın? ","Para yönetimini kendin mi yaparsın? ", "Meclis kararlarını takip eder misin? ",
"Kendinden küçüklerle konuşmayı sever misin? ", "Ülkenin yönetiminde söz sahibi olmak ister miyidin? ",
"Takım kaptanlığını mı yoksa üyeliğini mi tercih ederdin? ", "Sorumluluk sever misin? ", "İyi bi konuşmacı mısın? "]

m_sosyal_mv_cevap_list = ["-", "hayır", "evet", "-", "evet", "hayır", "evet", "üyelik", "evet", "evet"]
m_sosyal_yon_cevap_list = ["evet", "-", "-", "evet", "-", "-", "-", "kaptanlık", "evet", "-"]
m_sosyal_rehb_cevap_list = ["hayır", "evet", "hayır", "hayır", "hayır", "evet", "hayır", "-", "hayır", "evet"]


m_sozel_soru_list = ["İnsanları savunmayı sever misin? ", "Eğitim bölümünü düşündün mü? ", "Gündemi takip eder misin? ",
"Düzenli olarak kitap okur musun? ", "Araştrımacı mısındır? ", "Günlük tutar mısın? ", "Şiir yazmayı sever misin? ",
"Daha önce hiç suç hikayeleri okudun mu? ", "Haber okumayı sever misin? ", "Hiç röportaj yaptın mı? "]

m_sozel_yazar_cevap_list = ["hayır", "-", "hayır", "evet", "hayır", "evet", "evet", "-", "-", "hayır"]
m_sozel_basin_cevap_list = ["-", "hayır", "evet", "evet", "evet", "-", "hayır", "evet", "evet", "evet"]
m_sozel_adal_cevap_list = ["evet", "-", "-", "-", "evet", "-", "-", "evet", "-", "-"]


m_sayisal_soru_list = ["Bilime ilgi duyar mısın? ", "Günlük problem çözer misin? ", "Bilimsel belgeseller izler misin? ",
"Fizikle aran nasıldır? ", "Eğitim sektörünü düşündün mü? ", "Sayılarla aran iyi midir? ", "Sudoku sever misin? ",
"Bilimsel gelişmeleri takip eder misin? ", "Başkalarına matematik sorusu anlatabilir misin? ", "İnşaat sektörüne ilgi duyar mısın? "]

m_sayisal_muh_cevap_list = ["-", "evet", "-", "iyi", "hayır", "evet", "-", "-", "-", "evet"]
m_sayisal_fen_cevap_list = ["evet", "-", "evet", "iyi", "evet", "evet", "-", "evet", "-", "-"]
m_sayisal_mat_cevap_list = ["hayır", "evet", "hayır", "iyi", "evet", "evet", "evet", "hayır", "evet", "hayır"]


m_ortak_soru_list = ["İnsan anatomisini öğrenmek ister miydin? ", "Uçak kullanmak ister miydin? ", "Yazılım öğrenmeye ilgi duyuyor musun? ",
"Bilgisayar kullanmayı sever misiniz? ", "İnsanların dertlerini dinlemeyi sever misin? ", "İlk yardım biliyor musun? Öğrenmek ister misin? ",
"Araç içerikli bir meslek yapmayı ister miydin? ", "Oyun yapmak ister misin? ", "Hastaneleri sever misin? ", "Klavye kullanmada iyi misin? "]

m_ortak_yazilim_cevap_list = ["hayır", "hayır", "evet", "evet", "hayır", "hayır", "hayır", "evet", "hayır", "evet"]
m_ortak_tip_cevap_list = ["evet", "hayır", "hayır", "hayır", "evet", "evet", "hayır", "hayır", "evet", "hayır"]
m_ortak_pilotluk_cevap_list = ["hayır", "evet", "hayır", "hayır", "hayır", "hayır", "evet", "hayır", "hayır", "hayır"]


##Bölüm skorları:
sayisalp = 0
sozelp = 0
sosyalp = 0


##Meslek skorları:
#Sözel:
yazarlik = 0
basin_gazete = 0
adalet = 0

#Sayısal:
mat_ogrt = 0
fen_ogrt = 0
genel_muhendislik = 0

#Sosyal:
milletv = 0
yonetici = 0
rehberlik = 0

#Ortak Meslekler:
yazilim = 0
tip = 0
pilotluk = 0


print(f"Hangi Meslek Sana Göre?\n{50*'*'} \nİlk önce istediğiniz mesleğin bölümünü netleştirelim."
      "\n  *Eğer çıkmak isterseniz q yazabilirsiniz. "
      "\n  *Sorulara tek kelimelik kısa cevaplar veriniz. \n  *Büyük harf ve küçük harf fark etmemektedir."
      "\n  *Sayısal, sözel ve sosyal olmaz üzere 3 farklı bölüm vardır.\n  *Bölüm testimiz 10 sorudan oluşmaktadır."
      "\n  *Eğer birden fazla doğru seçenek varsa 'hepsi' yazınız."
      "\n  *Eğer şıklardan biri bile size yakın gelmiyorsa 'hiç', ikisi de doğru geliyorsa 'fark etmez' yazınız."
      "\n  *Soru sizin için doğruysa 'evet', çok doğruysa 'kesinlikle'; yanlışsa 'hayır', çok yanlışsa 'asla' yazınız.", end = "\n\n")

i = 0
while i < 10:
    cvp = input(b_soru_list[i])
    if cvp.lower() == b_sayisal_cevap_list[i]:
        sayisalp +=1
    elif cvp.lower() == b_sozel_cevap_list[i]:
        sozelp += 1
    elif cvp.lower() == b_sosyal_cevap_list[i]:
        sosyalp += 1
    elif cvp.lower() == "q":
        print("Çıkış Yapıyorsunuz")
        break
    else:
        print("Sanırım yazım hatası yaptın ya da cevabın şıklarda yok! Tekrar dene")
        continue
    i += 1

print("\nHangi bölüme gideceğini hesaplıyorummmmm!!")
for i in range(10):
    time.sleep(0.5)
    print("*", end = " ")

if sayisalp > sozelp and sayisalp > sosyalp:
    print("Sayısal yönün baskın çıktı...\nŞimdi hangi mesleğe gidici olduğunu bulalım!")
    print("  *Sınavımız 10 Sorudan oluşmaktadır.\n")
    i = 0
    bolum = "Sayısal"
    while i < 10:
        cvp = input(m_sayisal_soru_list[i])
        if cvp.lower() == m_sayisal_muh_cevap_list[i]:
            genel_muhendislik += 1
        elif cvp.lower() == m_sayisal_fen_cevap_list[i]:
            fen_ogrt += 1
        elif cvp.lower() == m_sayisal_mat_cevap_list[i]:
            mat_ogrt += 1
        elif cvp.lower() == "q":
            print("Çıkış yapıyorunusuz")
            break
        else:
            print("Sanırım yazım hatası yaptın ya da cevabın şıklarda yok! Tekrar dene")
            continue
        i += 1
    if genel_muhendislik > fen_ogrt and genel_muhendislik > mat_ogrt:
        meslek = "Mühendislik"
    elif mat_ogrt > fen_ogrt and mat_ogrt > genel_muhendislik:
        meslek = "Matematik Öğretmenliği"
    elif fen_ogrt > genel_muhendislik and fen_ogrt > mat_ogrt:
        meslek = "Fen Öğretmenliği"
    else:
        print("Sana net bir meslek bulamadım.. Belki biraz beklemen gerekiyordur.")
        meslek = "-"
elif sozelp > sayisalp and sozelp > sosyalp:
    print("Demek sözelcisin............\nNeyse şimdi seni sözelden bir yere postalayalım.")
    print("  *Sınavımız 10 Sorudan oluşmaktadır.\n")
    i = 0
    bolum = "Sözel"
    while i < 10:
        cvp = input(m_sozel_soru_list[i])
        if cvp.lower() == m_sozel_yazar_cevap_list[i]:
            yazarlik += 1
        elif cvp.lower() == m_sozel_adal_cevap_list[i]:
            adalet += 1
        elif cvp.lower() == m_sozel_basin_cevap_list[i]:
            basin_gazete += 1
        elif cvp.lower() == "q":
            print("Çıkış Yapıyorsunuz")
            break
        else:
            print("Sanırım yazım hatası yaptın ya da cevabın şıklarda yok! Tekrar dene")
            continue
    i += 1
    if yazarlik > basin_gazete and yazarlik > adalet:
        meslek = "Edebiyat Öğretmenliği"
    elif basin_gazete > adalet and basin_gazete > yazarlik:
        meslek = "Basın ya da Gazetecilik"
    elif adalet > basin_gazete and adalet > yazarlik:
        meslek = "Adalet"
    else:
        print("Sana net bir meslek bulamadım.. Belki biraz beklemen gerekiyordur.")
        meslek = "-"
elif sosyalp > sayisalp and sosyalp > sozelp:
    print("Sosyal bölümde başarı gösterdin! \nŞimdi sana bir meslek sınavı yapalım")
    print("  *Sınavımız 10 Sorudan oluşmaktadır.\n")
    i = 0
    bolum = "Sosyal"
    while i < 10:
        cvp = input(m_sosyal_soru_list[i])
        if cvp.lower() == m_sosyal_mv_cevap_list[i]:
            milletv += 1
        elif cvp.lower() == m_sosyal_yon_cevap_list[i]:
            yonetici += 1
        elif cvp.lower() == m_sosyal_rehb_cevap_list[i]:
            rehberlik += 1
        elif cvp.lower() == "q":
            print("Çıkış yapıyorusunuz")
            break
        else:
            print("Sanırım yazım hatası yaptın ya da cevabın şıklarda yok! Tekrar dene")
            continue
        i += 1
    if milletv > yonetici and milletv > rehberlik:
        meslek = "Millet Vekilliği(?)"
    elif yonetici > milletv and yonetici > rehberlik:
        meslek = "Yönetici"
    elif rehberlik > yonetici and rehberlik > milletv:
        meslek = "Rehberlik"
    else:
        print("Sana net bir meslek bulamadım.. Belki biraz beklemen gerekiyordur.")
        meslek = "-"
elif sosyalp == 0 and sozelp == 0 and sayisalp == 0:
    print("Vay be.. Demek.. Neyse! Hala çaycılık duruyor.")
    bolum = "-"
    meslek = "-"
else:
    print("Anlaşılan birden fazla dalda eşit başarı elde ettin! \nBu durumda seni ortak meslekler bölümünden sınav yapacağım...")
    print("  *Sınavımız 10 Sorudan oluşmaktadır.\n")
    i = 0
    bolum = "Eşit Ağırlık"
    while i < 10:
        cvp = input(m_ortak_soru_list[i])
        if cvp.lower() == m_ortak_tip_cevap_list[i]:
            tip += 1
        elif cvp.lower() == m_ortak_yazilim_cevap_list[i]:
            yazilim += 1
        elif cvp.lower() == m_ortak_pilotluk_cevap_list[i]:
            pilotluk += 1
        elif cvp.lower() == "q":
            print("Çıkış Yapıyorsunuz")
            break
        else:
            print("Sanırım yazım hatası yaptın ya da cevabın şıklarda yok! Tekrar dene")
            continue
        i += 1
    if pilotluk > yazilim and pilotluk > tip:
        meslek = "Pilotluk"
    elif yazilim > pilotluk and yazilim > tip:
        meslek = "Yazılım"
    elif tip > yazilim and tip > pilotluk:
        meslek = "Tıp"
    else:
        print("Sana net bir meslek bulamadım.. Belki biraz beklemen gerekiyordur.")
        meslek = "-"

print("\nSonuçların yükleniyor!!!")
for i in range(10):
    time.sleep(0.5)
    print("*", end = " ")

print(f"\nTüm testleri bitirmeyi başardın! \nŞimdi sonuçları açıklama vakti!!!"
    f"\nSayısal Puanın: {sayisalp}"
    f"\nSosyal Puanın: {sosyalp}"
    f"\nSözel Puanın: {sozelp}"
    f"\nKazandığın Bölüm: {bolum}"
    f"\nKazandığın Meslek: {meslek}")