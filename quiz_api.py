#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz Jurumiyah - Bab Kalam (الكلام)
- Sumber: Kitab Al-Ajurrumiyah (bab pertama: Kalam)
- Hanya mencakup definisi kalam, syarat-syaratnya, dan contoh.
- 10 soal pilihan ganda + penjelasan.
- Menyimpan hasil skor ke file results_TIMESTAMP.json

Author: ChatGPT (GPT-5)
"""
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load question bank
with open("questions.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

@app.route("/get_questions", methods=["GET"])
def get_questions():
    topic = request.args.get("topic")
    if topic in QUESTIONS:
        return jsonify(QUESTIONS[topic])
    return jsonify({"error": "Topic not found"}), 404

@app.route("/")
def home():
    return "Quiz API is running!"

import random
import json
import datetime
import sys

# ==========================
# Question Bank: Bab Kalam
# ==========================
QUESTION_BANK = {
    "Kalam (الكلام)": [
        {
            "q": "Definisi kalām menurut nahwu (ringkas) adalah:",
            "choices": [
                "Lafaz yang tersusun, memberi faidah sempurna, berdasarkan wad'i (bahasa Arab).",
                "Satu kata yang berdiri sendiri tanpa konteks.",
                "Tulisan di kertas yang bermakna.",
                "Isyarat tangan yang dimengerti."
            ],
            "a": 0,
            "ex": "Kalam menurut nahwu: lafẓ murakkab (lebih dari satu kata), mufīd (mendatangkan faedah sempurna), wad'i (berbahasa Arab)."
        },
        {
            "q": "Mana yang memenuhi syarat kalām?",
            "choices": ["زيدٌ", "زيدٌ قائمٌ", "في البيتِ", "إذا جاء زيدٌ ..."],
            "a": 1,
            "ex": "'زيدٌ قائمٌ' murakkab dan mufīd → kalām. 'زيدٌ' hanya kalimah. 'إذا جاء زيدٌ...' menggantung (tidak mufīd)."
        },
        {
            "q": "Syarat 'lafaz' dalam definisi kalām maksudnya:",
            "choices": [
                "Harus terdengar (diucapkan), bukan hanya tertulis.",
                "Boleh hanya tertulis di kertas.",
                "Bisa berupa isyarat tangan.",
                "Khusus untuk tulisan suci saja."
            ],
            "a": 0,
            "ex": "Lafaz = suara yang keluar dari mulut dan terdengar; definisi nahwu menekankan pengucapan, bukan sekadar tulisan."
        },
        {
            "q": "Mengapa 'إذا جاء زيدٌ...' tidak disebut kalām sempurna?",
            "choices": [
                "Karena susunan salah.",
                "Karena mengandung huruf yang tidak dikenal.",
                "Karena maknanya menggantung; pendengar menunggu kelanjutan.",
                "Karena bukan bahasa Arab."
            ],
            "a": 2,
            "ex": "Jika dimulai dengan حرف شرط seperti إذا, kalimat menjadi syarthiyah dan makna belum sempurna."
        },
        {
            "q": "Manakah yang bukan syarat kalām menurut definisi klasik?",
            "choices": [
                "Lafaz diucapkan",
                "Tersusun minimal dua kata",
                "Mengandung kata kerja (fi'il)",
                "Memberi faedah sempurna"
            ],
            "a": 2,
            "ex": "Kalam bisa berupa jumlah ismiyyah (tanpa fi'il). Jadi 'mengandung fi'il' bukan syarat."
        },
        {
            "q": "Contoh kalām isimiyyah (nominal sentence):",
            "choices": ["ذهبَ زيدٌ", "زيدٌ قائمٌ", "في السوقِ", "لم يأتِ"], 
            "a": 1,
            "ex": "Jumlah ismiyyah: 'زيدٌ قائمٌ' (mubtada' + khabar) — kalām."
        },
        {
            "q": "Kalām harus 'berdasarkan wad'i' maksudnya adalah:",
            "choices": [
                "Berbahasa Arab sesuai ketentuan bahasa.",
                "Ditulis rapi di kertas.",
                "Diucapkan dengan intonasi tinggi.",
                "Hanya untuk kalimat suci."
            ],
            "a": 0,
            "ex": "Wad'i = berdasarkan penetapan bahasa Arab (aturan bahasa). Kalimat dalam bahasa lain tidak disebut kalām menurut ilmu nahwu."
        },
        {
            "q": "Jika seseorang menulis 'زيد' di papan tulis tetapi tidak mengucapkannya, itu disebut:",
            "choices": [
                "Lafaz (lafẓ)",
                "Kalimah (الكلمة)",
                "Kalam (الكلام)",
                "Harf saja"
            ],
            "a": 1,
            "ex": "Teks tertulis bukan lafaz (suara). 'زيد' sebagai satu kata adalah kalimah."
        },
        {
            "q": "Dalam praktikum nahwu, mengapa penting membedakan kalām dan kalimah?",
            "choices": [
                "Agar bisa menerjemahkan ke bahasa lain lebih cepat.",
                "Karena aturan i'rab bergantung apakah itu kalām (susunan) atau kalimah (tunggal).",
                "Supaya bisa menulis lebih indah.",
                "Agar dapat membuat puisi."
            ],
            "a": 1,
            "ex": "Analisis i'rab memerlukan identifikasi apakah sebuah unit adalah kalām (kalimat) atau kalimah (kata tunggal)."
        },
        {
            "q": "Kalām yang mengandung huruf syarth (seperti إِذَا) biasanya:",
            "choices": [
                "Langsung mufīd tanpa lanjutan.",
                "Belum sempurna maknanya hingga klausa syarat dipenuhi.",
                "Bukan bahasa Arab.",
                "Harus diakhiri tanda tanya."
            ],
            "a": 1,
            "ex": "Huruf syarth membuat kalam menjadi syarthiyah; pendengar menunggu kelanjutan."
        },
    ]
}

# ===================================
# Fungsi untuk menjalankan kuis
# ===================================
def run_quiz():
    print("=== Quiz Jurumiyah: Bab Kalam (الكلام) ===")
    score = 0
    questions = QUESTION_BANK["Kalam (الكلام)"]
    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\n{i}. {q['q']}")
        for idx, choice in enumerate(q["choices"]):
            print(f"   {idx+1}. {choice}")
        try:
            ans = int(input("Jawabanmu (1-4): ")) - 1
        except:
            ans = -1

        if ans == q["a"]:
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah. Jawaban benar: {q['choices'][q['a']]}")
        print("Penjelasan:", q["ex"])

    print("\n=== Hasil Akhir ===")
    print(f"Skor: {score} / {len(questions)}")

    # simpan hasil
    result = {
        "timestamp": datetime.datetime.now().isoformat(),
        "score": score,
        "total": len(questions)
    }
    filename = f"results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"Hasil tersimpan di {filename}")

if __name__ == "__main__":
    run_quiz()