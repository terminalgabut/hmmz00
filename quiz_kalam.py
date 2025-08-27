
FILE: quiz_kalam.py

""" Quiz terminal interaktif untuk Bab Kalam & topik nahwu. Fitur:

Pilih topik (atau semua)

10 soal per topik (default soal dari bank)

Acak soal dan pilihan

Tampilkan penjelasan setelah menjawab

Simpan hasil ke file results_TIMESTAMP.json """ import random import json import datetime


QUESTION_BANK = { "Kalam": [ {"q":"Manakah yang memenuhi syarat kalam menurut nahwu?","choices":["زيدٌ","زيدٌ قائمٌ","في البيتِ","إذا جاء زيدٌ"],"a":1,"ex":"Kalam harus murakkab minimal dua kata dan mufid. 'زيدٌ قائمٌ' memenuhi."}, {"q":"Kalām harus memenuhi syarat apa saja?","choices":["lafaz, murakkab, mufid, wad'i","lafaz saja","murakkab dan lafaz saja","hanya mufid"],"a":0,"ex":"Empat syarat: lafaz (diucapkan), murakkab (tersusun), mufid (mendatangkan faedah sempurna), wad'i (bahasa Arab)."}, {"q":"Apakah 'في المدرسة' termasuk kalam?","choices":["Ya, karena berbahasa Arab","Tidak, karena menggantung","Ya, karena dua kata","Tidak, karena bukan lafaz"],"a":1,"ex":"'في المدرسة' belum mufid sempurna (menggantung sebagai keterangan tempat saja)."}, {"q":"Contoh kalam verbal adalah...","choices":["الولدُ طويلٌ","جلسَ زيدٌ","في الحديقةِ","من المدرسةِ"],"a":1,"ex":"'جلسَ زيدٌ' adalah kalam fi'li (verbal sentence)."}, {"q":"Jika sebuah susunan kata memberi faedah sempurna disebut...","choices":["kalimah","kalam","harf","fi'il"],"a":1,"ex":"Definisi mufid mengarah pada kalam (kalām)."}, {"q":"Apakah tulisan di kertas tanpa pengucapan disebut lafaz?","choices":["Ya","Tidak","Kadang-kadang","Hanya bila ada alif-lam"],"a":1,"ex":"Lafaz diartikan sebagai suara yang keluar dari mulut, bukan tulisan."}, {"q":"Mana yang bukan syarat kalam?","choices":["Diucapkan","Tersusun minimal dua kata","Berbahasa Arab","Berisi kata kerja"],"a":3,"ex":"Tak harus mengandung kata kerja; jumlah isimiyyah juga bisa menjadi kalam."}, {"q":"Kalām dalam bahasa selain Arab dianggap?","choices":["Sah sebagai kalam nahwu","Bukan kalam menurut nahwu","Sah jika bermakna","Hanya jika diterjemahkan"],"a":1,"ex":"Kalam menurut definisi nahwu harus berbahasa Arab."}, {"q":"Manakah yang disebut kalimah?","choices":["زيدٌ","زيدٌ قائمٌ","إن جاء زيدٌ","لم يكتب"],"a":0,"ex":"Kalimah adalah satu kata; 'زيدٌ' contoh isim (kalimah)."}, {"q":"Mengapa 'إذا جاء زيدٌ...' disebut menggantung?","choices":["Karena huruf syarth tidak lengkap","Karena mengandung isim saja","Karena bukan bahasa Arab","Karena tidak diucapkan"],"a":0,"ex":"'إذا' membutuhkan kelanjutan sehingga makna belum sempurna."} ], "Kalimah": [ {"q":"Apa itu kalimah?","choices":["Satu kata yang bermakna","Satu kalimat lengkap","Hanya isim","Hanya harf"],"a":0,"ex":"Kalimah (الكلمة) adalah lafaz tunggal yang berisi makna (bisa isim/fi'il/harf)."}, {"q":"Kalimah dibagi menjadi berapa?","choices":["2","3","4","5"],"a":1,"ex":"Tiga: isim, fi'il, harf."}, {"q":"Manakah contoh fi'il?","choices":["ذهبَ","كتابٌ","في","هذا"],"a":0,"ex":"'ذهبَ' adalah fi'il (kata kerja)."}, {"q":"'يا' termasuk apa?","choices":["Isim","Fi'il","Harf (nida')","Kalimah tidak"],"a":2,"ex":"'يا' adalah huruf nida' (harf)."}, {"q":"Kata 'في' termasuk...","choices":["Isim","Fi'il","Harf jar","Kalimah tidak"],"a":2,"ex":"'في' adalah huruf jar (preposisi)."}, {"q":"Apakah semua kalimah menjadi kalam?","choices":["Ya","Tidak","Hanya isim","Hanya fi'il"],"a":1,"ex":"Sebuah kalimah tunggal belum tentu menjadi kalam; harus jadi murakkab mufid."}, {"q":"Sebuah kata punya tanwin biasanya...","choices":["Isim nakirah","Isim ma'rifah","Harf","Fi'il"],"a":0,"ex":"Tanwin menandakan isim nakirah biasanya."}, {"q":"'محمدٌ' adalah contoh...","choices":["Isim","Fi'il","Harf","Kalimah tidak"],"a":0,"ex":"Muhammad adalah ism (nama)."}, {"q":"Harf yang memanggil seseorang disebut...","choices":["نida'","jar","ta' marbuta","isim"],"a":0,"ex":"Nida' adalah huruf panggilan seperti 'يا'."}, {"q":"Kalimah yang menjelaskan waktu biasanya...","choices":["Isim waktu","Fi'il","Harf","Tidak mungkin"],"a":0,"ex":"Banyak kata yang menyatakan waktu adalah isim (zaman)."} ], "Isim": [ {"q":"Ciri utama isim adalah...","choices":["Terikat waktu","Tidak terikat waktu","Harus punya alif-lam","Selalu berakhiran nun"],"a":1,"ex":"Isim menunjukkan makna tanpa terikat waktu (berbeda dengan fi'il)."}, {"q":"Manakah yang merupakan isim?","choices":["كتبَ","محمدٌ","يذهبُ","لم"],"a":1,"ex":"'محمدٌ' adalah isim (nama)."}, {"q":"'هو' termasuk jenis apa?","choices":["Fi'il","Isim (dhamir)","Harf","Tidak satupun"],"a":1,"ex":"Dhamir termasuk kategori isim."}, {"q":"Isim yang diberi ال menjadi...","choices":["Nakirah","Ma'rifah","Fi'il","Harf"],"a":1,"ex":"Alif-lam mengubah nakirah menjadi ma'rifah."}, {"q":"'هذا' termasuk...?","choices":["Harf","Isim isyarah","Fi'il","Kalimah tidak"],"a":1,"ex":"'هذا' penunjuk (isim isyarah)."}, {"q":"Tanwin biasanya menandakan...","choices":["Isim nakirah","Isim ma'rifah","Fi'il","Harf"],"a":0,"ex":"Tanwin umum menandai isim nakirah."}, {"q":"Contoh isim mabni biasanya...","choices":["هو، أنا، هذا","كتابٌ، مسجدٌ","كتبَ، ذهبَ","في، على"],"a":0,"ex":"Dhamir, ism isyarah sering bersifat mabni (tidak ber-i'rob seperti biasa)."}, {"q":"Kata setelah huruf jar biasanya...","choices":["Fi'il","Isim majrur","Harf jar","Tanwin"],"a":1,"ex":"Huruf jar menyebabkan isim setelahnya menjadi majrur."}, {"q":"Isim ma'rifah contoh...","choices":["كتابٌ","الكتابُ","رجلٌ","مدينةٌ"],"a":1,"ex":"'الكتابُ' adalah ma'rifah karena ada alif-lam."}, {"q":"'سوقٌ' termasuk...?","choices":["Isim nakirah","Isim ma'rifah","Harf","Fi'il"],"a":0,"ex":"'سوقٌ' sebuah pasar, nakirah."} ], "Huruf_Jar": [ {"q":"Apa efek huruf jar pada isim setelahnya?","choices":["Jadi marfu'","Jadi majrur (berkasrah)","Jadi mansub","Tidak berubah"],"a":1,"ex":"Huruf jar menajdi majrur sehingga akhir isim berkasrah."}, {"q":"Manakah bukan huruf jar?","choices":["من","هل","إلى","على"],"a":1,"ex":"'هل' adalah huruf istifham, bukan huruf jar."}, {"q":"Huruf jar yang bermakna 'ke' adalah...","choices":["من","إلى","عن","على"],"a":1,"ex":"إلى berarti ke/hingga."}, {"q":"Huruf yang menunjukkan tempat 'di dalam' adalah...","choices":["على","في","من","رب"],"a":1,"ex":"'في' berarti di dalam/pada."}, {"q":"Huruf jar yang sering diikuti isim nakirah dan menuntut fathah disebut...","choices":["من","رب","باء","كاف"],"a":1,"ex":"'ربَّ' (rubba) biasanya diikuti isim nakirah dan mengikuti aturan berbeda."}, {"q":"'بِالكتابِ' penggunaan hurufnya adalah...","choices":["باء (dengan)","من","في","كاف"],"a":0,"ex":"'بِ' berfungsi sebagai alat/wasilah (dengan)."}, {"q":"Huruf yang menandakan perbandingan (seperti) adalah...","choices":["من","كاف","في","رب"],"a":1,"ex":"كاف untuk tasybih (seperti)."}, {"q":"Setelah huruf jar, bentuk i'rob pada isim biasanya...","choices":["berkasrah atau tanda jar lain","berfathah","berdhammah","tetap"],"a":0,"ex":"Majrur: kasrah atau tanda jar sesuai aturan."}, {"q":"Contoh kalimat dengan huruf jar 'على'","choices":["على الطاولةِ","ذهبَ الطالبُ","الكتابُ جديدٌ","إن جاء زيدٌ"],"a":0,"ex":"'على الطاولةِ' benar: 'على' huruf jar dan الطاولة majrur."}, {"q":"Huruf 'باء' dipakai untuk...","choices":["asal","penyebab/alat","perbandingan","penunjuk waktu"],"a":1,"ex":"باء sering berarti 'dengan' atau 'oleh karena'."} ] }

ALL_TOPICS = list(QUESTION_BANK.keys())

def ask_quiz(topic, num_questions=10): bank = QUESTION_BANK[topic][:] random.shuffle(bank) selected = bank[:num_questions] score = 0 answers = [] for i, item in enumerate(selected,1): print(f"\n{i}. {item['q']}") choices = item['choices'][:] random.shuffle(choices) for idx, ch in enumerate(choices): print(f"  {idx+1}. {ch}") # map shuffled index to correct correct_text = item['choices'][item['a']] answer = input("Jawab (nomor): ").strip() if not answer.isdigit() or not (1 <= int(answer) <= len(choices)): print("Input tidak valid, dianggap salah.") correct_idx = choices.index(correct_text) print(f"Jawaban benar: {correct_idx+1}. {correct_text}") answers.append({'q':item['q'],'your':None,'correct':correct_text,'ex':item['ex']}) continue pick = choices[int(answer)-1] if pick == correct_text: print("Benar!") score += 1 else: print("Salah.") print(f"Jawaban benar: {correct_text}") print(f"Penjelasan: {item['ex']}") answers.append({'q':item['q'],'your':pick,'correct':correct_text,'ex':item['ex']}) return score, answers

def main(): print("QUIZ KALAM & NAHWU - Terminal") print("Topik tersedia:") for i,t in enumerate(ALL_TOPICS,1): print(f"  {i}. {t}") print(f"  {len(ALL_TOPICS)+1}. Semua topik (acak)") choice = input("Pilih topik (nomor): ").strip() if not choice.isdigit(): print("Input invalid. Keluar.") return c = int(choice) if c == len(ALL_TOPICS)+1: topic = 'ALL' elif 1 <= c <= len(ALL_TOPICS): topic = ALL_TOPICS[c-1] else: print("Pilihan tidak tersedia.") return

if topic == 'ALL':
    total_score = 0
    total_answers = []
    for t in ALL_TOPICS:
        print(f"\n--- Topik: {t} ---")
        s,a = ask_quiz(t, num_questions=min(10,len(QUESTION_BANK[t])))
        total_score += s
        total_answers.extend(a)
    max_score = sum(min(10,len(QUESTION_BANK[t])) for t in ALL_TOPICS)
    print(f"\nTotal skor: {total_score}/{max_score}")
else:
    s,a = ask_quiz(topic, num_questions=min(10,len(QUESTION_BANK[topic])))
    print(f"\nSkor: {s}/{min(10,len(QUESTION_BANK[topic]))}")
    total_score = s
    total_answers = a
    max_score = min(10,len(QUESTION_BANK[topic]))
# simpan hasil
now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
out = {'timestamp':now,'topic':topic,'score':total_score,'max':max_score,'answers':total_answers}
fname = f'results_{now}.json'
with open(fname,'w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
print(f"Hasil tersimpan di {fname}")

if name=='main': main()
