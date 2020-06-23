#beden kütle endeksi - Sağlık göstergesi hesaplama

print("Beden Kitle Endeksi")
kilo = float (input ("Lütfen ağırlığınızı(kg) giriniz: "))
boy = float (input ("Lütfen boyunuzu(cm) giriniz: "))
boy = boy/100.0
bki = kilo / (boy ** 2)
i_kilo = 18.5 * boy ** 2
print("Beden kitle endeksiniz: " , bki)
cumle = "Olmanız gereken kilo: "
if bki < 18.5:
    print("Zayıfsınız.")
    print("Sağlıklı biçimde kilo alabilirsiniz." , cumle, i_kilo)
elif 18.5 < bki < 24.9:
    print("Sağlıklısınız.")
    print("Kilonuzu koruyunuz.")
elif 25 < bki < 29.9:
    print("Biraz kilolusunuz.")
    print("Düzenli beslenerek sağlıklı olan kilonuza düşebilirsiniz." , cumle, i_kilo)
elif 30 < bki < 34.9:
    print("1.derece Obezsiniz.")
    print("Sağlıklı olabilmeniz için kilo vermeniz gerekiyor." , cumle, i_kilo)
elif 35 < bki < 39.9:
    print("2.derce Obezsiniz.")
    print("Lütfen diyet yaparak sağlıklı kilonuza kavuşun." , cumle, i_kilo)
else:
    print("Tebrikler! Artık obezliğin 3. bölümüne ulaştınız.")
    print("Sağlığınıza kavuşmak istiyorsanız kilo verin!" , cumle, i_kilo)
