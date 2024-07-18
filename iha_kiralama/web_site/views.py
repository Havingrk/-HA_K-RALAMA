from django.http.response import HttpResponse

from django.shortcuts import render

data={
    "blogs": [
        {
            "id":1,
            "marka":"baykar",
            "model":"TB1",
            "image":"tb1.jpeg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"Türkiye’de Baykar tarafından üretilen bir insansız hava aracıdır.Keşif ve istihbarat görevleri için orta irtifa-uzun havada kalış süresi sınıfına giren (MALE) bir insansız hava aracıdır.",
            
        },
        {
            "id":2,
            "marka":"baykar",
            "model":"TB2",
            "image":"tb2.jpeg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"Türk havacılık tarihinde havada kalma süresi ve irtifa rekorunu kırmıştır.Gelişmiş özellikleri arasında tam otomatik seyir ve rota takibi, dahili sensör füzyonu destekli hassas otomatik kalkış ve iniş bulunur.",
            
        },
        {
            "id":3,
            "marka":"baykar",
            "model":"TB3",
            "image":"tb3.jpeg",
            "ağırlık":"1,450kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"Kısa pistli gemilerden kalkış ve iniş kabiliyetine sahip silahlı bir insansız hava aracıdır.Deniz aşırı görevlerde kullanılabilir ve yerleşik lazer hedef işaretleyicisi ile hassas hedefleme yapabilir.",
            
        },
        {
            "id":4,
            "marka":"tusaş",
            "model":"ANKA",
            "image":"anka.jpeg",
            "ağırlık":"350kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"Türk Havacılık ve Uzay Sanayii (TUSAŞ) tarafından üretilen bir insansız hava aracıdır. ANKA, keşif, istihbarat ve gözetleme görevleri için tasarlanmıştır. Yüksek irtifada uzun süre havada kalabilme yeteneği ve çeşitli sensörlerle donatılması, operasyonel etkinliğini artırır.",
            
        },
        {
            "id":5,
            "marka":"tusaş",
            "model":"ANKA-3",
            "image":"anka3.jpg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"ANKA-3 ile keşif, gözetleme ve istihbarat toplanması, milli mühimmatlarla havadan karaya taarruz, hava-hava mühimmatları ile de düşman helikopter, uçak ve İHA’larını avlaması, düşük radar iziyle (stealth ucav) düşman radar ve hava savunma sistemlerinin etkisiz hale getirilmesi görevlerinde yer alabilmektedir.",
            
        },
        {
            "id":6,
            "marka":"tusaş",
            "model":"ANKSUNGUR",
            "image":"AKSUNGUR.jpeg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"Sistem kesintisiz, gündüz/gece İstihbarat Gözetleme, Keşif ve Taarruz Görevleri için EO/IR, SAR ve SIGINT faydalı yükleri ve çeşitli havadan yere silahlarla icra eden Orta İrtifa Uzun Havada Kalışlı bir İnsansız Hava Aracı Sistemidir.",
            
        },
        {
            "id":7,
            "marka":"baykar",
            "model":"akıncı",
            "image":"akıncı.jpeg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"Akıncı İnsansız Hava Aracı (İHA), Türk Havacılık ve Uzay Sanayii tarafından geliştirilen bir stratejik istihbarat ve taarruz platformudur. Uzun menzili, yüksek irtifada görev yapabilme kabiliyeti ve çeşitli silah sistemlerini taşıma yeteneği ile öne çıkar.",
            
        },
        {
            "id":8,
            "marka":"havelsan",
            "model":"BAHA",
            "image":"baha.jpeg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":True,
            "açıklama":"Türkiye'nin geliştirdiği bir hava aracı platformudur. İstihbarat toplama, keşif ve gözetleme görevlerini yerine getirebilir ve hafif silah taşıma kapasitesine sahiptir.",
            
        },
        {
            "id":9,
            "marka":"aselsan",
            "model":"SERÇE",
            "image":"tb1.jpeg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":False,
            "açıklama":"Türkiye tarafından geliştirilen küçük ölçekli bir hava aracı platformudur. Özellikle yerli ve milli olarak tasarlanan bu İHA, hafif görevler için kullanılmak üzere tasarlanmıştır ve genellikle keşif ve gözetleme amaçlarıyla kullanılır.",
            
        },
        {
            "id":10,
            "marka":"vestel",
            "model":"KARAYEL",
            "image":"tb1.jpeg",
            "ağırlık":"1,5kg",
            "kanat_açıklığı":"",
            "uzunluk":"",
            "yükseklik":"",
            "kiralama_durumu":False,
            "açıklama":"Türkiye'de geliştirilen orta irtifa ve uzun süreli uçuş kabiliyetine sahip bir platformdur. İstihbarat, keşif, gözetleme ve hedef tespit gibi çeşitli görevler için kullanılmaktadır ve farklı sensörlerle donatılabilme özelliğine sahiptir.",
            
        },
       
    ]
}


# Create your views here.
def index(request):
    context ={
        "blogs": data["blogs"]
    }
    return render(request, "website\index.html",context)
#render metodu bır kaynagı kullanıcıya gönderebilir.
def website(request):
    context ={
        "blogs": data["blogs"]
    }
    return render(request, "website\website.html",context)

def website_details(request,id):
    blogs = data["blogs"]
    selectedBlog = None
    for blog in blogs:
        if blog["id"] == id:
            selectedBlog = blog
           


    return render(request, "website\website_details.html", {
        "blog":selectedBlog
    })
    