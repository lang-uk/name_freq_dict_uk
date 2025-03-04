# Частотний словник українських імен на основі ubertext

[English version](README_en.md)

Згенеровано на основі:
1. [ubertext](https://lang.org.ua/en/ubertext/), а саме — [словника частот лем](https://lang.org.ua/static/downloads/ubertext2.0/dicts/ubertext_freq.csv.xz);
2. списка українських [чоловічих](https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D1%85_%D1%87%D0%BE%D0%BB%D0%BE%D0%B2%D1%96%D1%87%D0%B8%D1%85_%D1%96%D0%BC%D0%B5%D0%BD) і [жіночих](https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D1%85_%D0%B6%D1%96%D0%BD%D0%BE%D1%87%D0%B8%D1%85_%D1%96%D0%BC%D0%B5%D0%BD) імен з вікіпедії;
3. списка [українських прізвищ](https://uk.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D1%96%D1%8F:%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D1%96_%D0%BF%D1%80%D1%96%D0%B7%D0%B2%D0%B8%D1%89%D0%B0) з вікіпедії;
4. підсловника по-батькові з [ВЕСУМу](https://github.com/brown-uk/dict_uk).

Вже згенерований словник знаходиться у папці `generated`, який складається з 5 файлів:

- `lname_freq_dict.csv` — частотний словник прізвищ;
- `female_fname_freq_dict.csv` — частотний словник жіночих імен;
- `female_pname_freq_dict.csv` — частотний словник жіночих по-батькові;
- `male_fname_freq_dict.csv` — частотний словник чоловічих імен;
- `male_pname_freq_dict.csv` — частотний словник чоловічих по-батькові.

## Генерація словника

Не потребує окремих залежностей, лише необхідно мати доступ до інтернету для завантаження файлу `ubertext_freq.csv.xz`.

```bash
python3 generate_names_freq_dict.py
```

Додатково, можна розширити список виключень, додавши нові імена до файлу `ignore_list.txt`.

## Обмеження

Наразі, частотний словник лем має недосконалу токенізацію. А саме, можуть зустрічатись проблеми з іменами, що місять апострофи, дефіси, а також імена, котрі зустрічались в markdown-текстах. 
