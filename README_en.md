# Frequency Dictionary of Ukrainian Names Based on ubertext

Generated based on:
1. [ubertext](https://lang.org.ua/en/ubertext/), specifically – [frequency lemma dictionary](https://lang.org.ua/static/downloads/ubertext2.0/dicts/ubertext_freq.csv.xz);
2. The list of Ukrainian [male](https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D1%85_%D1%87%D0%BE%D0%BB%D0%BE%D0%B2%D1%96%D1%87%D0%B8%D1%85_%D1%96%D0%BC%D0%B5%D0%BD) and [female](https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D1%85_%D0%B6%D1%96%D0%BD%D0%BE%D1%87%D0%B8%D1%85_%D1%96%D0%BC%D0%B5%D0%BD) names from Wikipedia;
3. The list of Ukrainian [surnames](https://uk.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D1%96%D1%8F:%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B8_%D0%BF%D1%80%D1%96%D0%B7%D0%B2%D0%B8%D1%89%D0%B0) from Wikipedia;
4. A sub-dictionary of patronymics from [VESUM](https://github.com/brown-uk/dict_uk).

The generated dictionary is located in the `generated` folder, which consists of 5 files:

- `lname_freq_dict.csv` — frequency dictionary of surnames;
- `female_fname_freq_dict.csv` — frequency dictionary of female first names;
- `female_pname_freq_dict.csv` — frequency dictionary of female patronymics;
- `male_fname_freq_dict.csv` — frequency dictionary of male first names;
- `male_pname_freq_dict.csv` — frequency dictionary of male patronymics.

## Dictionary Generation

No additional dependencies are needed; you only require internet access to download the file `ubertext_freq.csv.xz`.

```bash
python3 generate_names_freq_dict.py
