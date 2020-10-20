# SaniML
Oyunlaştırılmış bir sosyal sorumluluk projesi


Dosyalara ait açıklama: 

        data.zip içerisinde:
                saniml-data dosyasında işlenmemiş ve split edilmemiş data bulunmaktadır.
                saniml-train-test-validation dosyasında resize edilmiş ve split edilmiş işlenmeye hazır data bulunmaktadır.
        saniml-demo-video.MOV:
                oluşturulan demo tanıtım videosudur.
        saniml.xd:
                saniml-demo-video.MOV un oluşturulduğu adebe xd çalışmasıdır.
        flask.zip:
                modelimizi online olarak deneyebileceğimiz bir arayüz oluşturmayı amaçladık.
                (not: güncel durumda, son aşamsında 405 hatası almaktayız.)
        saniml.ipynb:
                modelin eğitildiği ve kaydedildiği notebooktur.
        
        
Grup : SaniML


Takım : 

        Arzu Yılmaz            (yilmazarzu.98@gmail.com)
        Ecem Nur Yıldızcan  (ecemnuryildizcan@gmail.com)
        Elif Damla Karakolcu  (karakolcudamla@gmail.com)
        Tugay Bayrak          (tugay.bayrak98@gmail.com)
        
        

Arzu yılmaz: İstanbul Üniversitesi Sosyoloji bölümü üçüncü sınıf öğrencisi. Aynı zamanda ikinci üniversite olarak Anadolu üniversitesinde marka iletişimi öğrenimi görmekte. Projede, fikrin kurgulanması, mantıksal hataların gideilmesinden sorumlu.

Ecem Nur Yıldızcan: İstanul Üniversitesi Matematik bölümü son sınıf öğrencisi. TÜBİTAK'tan BİGG desteği almış ve Acıbadem Üniversitesi kuluçka merkezi bünyesinde şirkete dönüştürülen Auctifera Scientific kurumunda görüntü işleme mühendisi olarak yarı zamanlı çalışmakta ve projenin yazılım ekibi lideri görevinde. İstanbul Üniversitesi Bilgisayar Bilimleri Uygulama ve Araştırma Merkezi'nde bulunan yapay zeka laboratuvarının sorumlusu. Karmaşık Sistemler ve Veri Bilimi adlı toplulukta görüntü işleme üzerine araştırmalar yapmakta. Projede fikrin teknolojiye uyarlaması ve teknolojinin geliştirilmesinden sorumlu.

Elif Damla Karakolcu: İstanbul Üniversitesi Moleküler Biyoloji ve Genetik bölümü birinci sınıf öğrencisi. İkinci üniversite olarak İstanbul Üniversitesi'nde Yönetim Bilişim Sistemleri okuyor. İstanbul Üniversitesi Google DSC 'de genel sekreterlik görevini sürdürmekte. İstanbul Üniversites 3B Tetlab bünyesinde gerçekleşmiş Dijital Ameliyathane projesinde proje stajyeri olarak yer aldı. Projede, proje liderliği görevini üstlenmekte.

Tugay Bayrak: Anadolu Üniversitesi Hukuk Fakültesi son sınıf öğrencisi. İkinci üniversite olarak Anadolu üniversitesinde İşletme okumakta. Projede, başta sokak hayvanlarının sonrasında teknoloji kullanıcın ve üreticinin hakları konusunda doğru değerlendirme yapılması ve haklara uygun hareket edilmesinden sorumlu.


Projenin özeti: 

        Şehirler geliştikçe sokak hayvanlarının yaşam alanları kısıtlanmaya ve gıdaya ulaşımları zorlaşmaya başladı. Amacımız sokak hayvanlarının da sahiplenilmiş bir hayvan
        kadar destek görebilmesini sağlamak. Biz bunun için ilk adım olarak mama desteğini hayata geçirmek istiyoruz. Bu proje ile sokakta yaşayan bir hayvanın da eve alınmadan
        evlat edinilebileceğini göstermeyi planlıyoruz. Bunu da sokak gönüllüleri fikri ile ortaya atıyoruz. İlk adımda sokak gönüllülerinin, sorumluluğunu üstlendiği bölgede
        bulunan mama kabını fotoğraflayarak algoritmaya vermesini bekleyeceğiz. Kullanıcıların verdiği görseli dolu veya boş olarak etiketleyecek olan makine öğrenmesi
        algoritması çalıştığında, kullanıcının her dolu mama kabı girdisi için 1 puan verecek. Kullanıcı 10 puan topladığında bir ödül alacak ve puanı sıfırlanacak. 
        Bu uygulama ile aslında sorumluluk olarak üstlendiği ve gönüllü olarak yapacağı bu işi oyunlaştırarak zevkli ve daha yapılabilir hale getirmeyi planlıyoruz. 
    

Projenin yenilikçi yönü: 

        -Kişiselleştirilmiş teknoloji kullanımı deneyimi
        -Görüntü işleme teknolojisi
        -Gamification
        -Makine Öğrenmesi:
           -Binary sınıflandırma(keras)


Kütüphaneler ve Modüller : 

        PIL, Os, Keras, Numpy, Math, Matplotlib.pyplot, Random, Glob, Pandas, cv2, flask, skimage
        layers (from keras)
        models (from keras)
        mnist (from keras.datasets)
        Sequential (from keras.models)
        Activation, Dropout, Flatten, Dense (from keras.layers)
        Conv2D, MaxPooling2D (from keras.layers)
        ImageDataGenerator (from keras.preprocessing.image)
        backend (from keras)
        gc (Garbage Collector)
        load_model (from tensorflow.keras.models)
        ImageDataGenerator (from keras.preprocessing.image)
        

        

  

