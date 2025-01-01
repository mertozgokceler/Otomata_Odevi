DFA Simülatörü

Bu proje, belirli bir deterministik sonlu otomatı (DFA) kullanarak verilen bir girdinin DFA tarafından kabul edilip edilmediğini adım adım simüle eden bir Tkinter tabanlı Python uygulamasıdır.

Özellikler :

Kullanıcı girişi alır ve DFA'ya uygunluğunu kontrol eder.

DFA'nın her adımda hangi durumdan hangi duruma geçtiğini görüntüler.

Kabul veya reddetme sonucunu ekranda görüntüler.

Nasıl Çalışır ?

DFA Geçiş Tablosu:

DFA'nın durumları ve bu durumlar arasındaki geçişler dfa_transitions sözlük yapısı ile tanımlanır.

Kabul durumları dfa_accept_states kümesiyle tanımlanır.

Simüle Et Butonu:

Kullanıcının girdisini alır ve DFA adım adım simüle edilir.

Geçerli olmayan girdi veya geçiş durumları hata olarak belirtilir.

Sonuç Görüntüleme:

DFA'nın geçtiği adımlar ve son durum ekranda görüntülenir.

Girdi DFA tarafından kabul ediliyorsa "Kabul" yazısı, aksi takdirde "Reddedildi" yazısı görülür.

Kullanım

Girdiyi Girin:

Uygulamadaki metin kutusuna DFA tarafından kontrol edilmesini istediğiniz dizgeyi girin.

Simüle Et Butonuna Basın:

DFA tarafından adım adım kontrol edilir ve sonuç ekranda gösterilir.

Aşağıda DFA tablomuzu nasıl tanımladığımızı görüyoruz : 

dfa_transitions = {
    'q0': {'a': 'q2', 'b': 'q1'},
    'q1': {'a': 'q4', 'b': 'q3'},
    'q2': {'a': 'q5', 'b': 'q4'},
    'q3': {'a': 'q6', 'b': 'q3'},
    'q4': {'a': 'q7', 'b': 'q6'},
    'q5': {'a': 'q5', 'b': 'q7'},
    'q6': {'a': 'q8', 'b': 'q6'},
    'q7': {'a': 'q7', 'b': 'q8'},  
    'q8': {'a': 'q8', 'b': 'q8'},
}
