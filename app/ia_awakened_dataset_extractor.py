import json
import xml.etree.ElementTree as ET
import re

tree = ET.parse("./ia_all.xml")
root = tree.getroot()

collection = ["[Al-Muntakhab]", "[The Monotheist Group] (2011 Edition)", "[The Monotheist Group] (2013 Edition)", 
              "Abdel Haleem", "Abdul Hye", "Abdul Majid Daryabadi", "Ahmed Ali", "Ahmed Hulusi", "Ahmed Raza Khan (Barelvi)",
              "Aisha Bewley", "Ali Ãœnal", "Ali Quli Qara'i", "Amatul Rahman Omar", "Arabic", "Arthur John Arberry", 
              "Bakhtiari Nejad", "Bijan Moeinian", "Bilal Muhammad 2018", "Bridges", "Corpus.Quran", "Dr. Kamal Omar",
              "Dr. Laleh Bakhtiar", "Dr. Mohammad Tahir-ul-Qadri", "Dr. Munir Munshey", "Edward Henry Palmer",
              "Faridul Haque", "Fode Drame", "George Sale", "Hamid S. Aziz", "Hasan Al-Fatih Qaribullah",
              "Hilali - Khan", "Irving/Hegab", "John Medows Rodwell", "Linda &quot;iLham&quot; Barto", "M. Farook Malik",
              "Maududi", "Maulana Muhammad Ali", "Mir Aneesuddin", "Mohammad Shafi", "Muhammad Ahmed - Samira",
              "Muhammad Asad", "Muhammad H. al-`Asi", "Muhammad Mahmoud Ghali", "Muhammad Marmaduke Pickthall",
              "Muhammad Sarwar", "Muhammad Taqi Usmani", "Munir Mezyed", "MunirMezyed2023", "Musharraf Hussain", 
              "Mustafa Khattab 2018", "Mustaqim", "N J Dawood 2014 ", "OLD Word by Word", "Rashad Khalifa",
              "Safi Kaskas", "Safi Kaskas 2024", "Sam Gerrans", "Samy Mahdy", "Sayyed Abbas Sadr-Ameli",
              "Shabbir Ahmed", "Shakir", "Sher Ali", "Syed Vickar Ahamed", "T.B.Irving", "Talal Itani &amp;amp; AI (2024)", 
              "Talal Itani (2012)", "The Study Quran", "The Wise Quran", "Thomas Cleary", "Torres Al Haneef (partial translation)",
              "Transliteration", "Transliteration-2", "Umm Muhammad (Sahih International)", "Wahiduddin Khan",
              "Word by Word (2021)", "Word-For-Word (2020)", "Yahiya Emerick", "Yusuf Ali (Orig. 1938)", "Yusuf Ali (Saudi Rev. 1985)"
              ]


def is_equal(val1, val2):
    return val1 == val2

def clean_string(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    cleaned_string = re.sub(r'[^\w\s]', '', cleaned_string)
    return cleaned_string.replace(' ', '_')  

for idx, author in enumerate(collection):
    arr = {}

    for surah in root.findall(".//Surah"):
        surah_number = surah.get("SurahNumber")
        surah_transliterated_name = surah.get("SurahTransliteratedName")
        surah_arabic_name = surah.get("SurahArabicName")
        surah_english_name = surah.get("SurahEnglishNames")

        arr[int(surah_number)] = {}
        arr[int(surah_number)]["SurahTransliteratedName"] = surah_transliterated_name
        arr[int(surah_number)]["SurahArabicName"] = surah_arabic_name
        arr[int(surah_number)]["SurahEnglishNames"] = surah_english_name
        arr[int(surah_number)]["Ayahs"] = {}

        for ayah in surah.findall("Ayah"):
            ayah_number = ayah.get("AyahNumber")
            arr[int(surah_number)]["Ayahs"][int(ayah_number)] = {}
            for rendition in ayah.findall("Rendition"):
                source = rendition.get("Source")
                text = rendition.text
                if source == collection[idx]:
                    arr[int(surah_number)]["Ayahs"][int(ayah_number)][source] = text

    file_name = "./collection/" + clean_string(collection[idx]) + ".json"
    with open(file_name, "w") as file:
        json.dump(arr, file, indent=4)



