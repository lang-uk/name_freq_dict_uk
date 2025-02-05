import csv
import os
import urllib.request
import lzma
import shutil

# Ensure the target directory exists
os.makedirs('dict', exist_ok=True)

def reporthook(block_num, block_size, total_size):
    downloaded = block_num * block_size
    if total_size > 0:
        percent = downloaded * 100 / total_size
        print(f"Downloading: {percent:.2f}% complete", end='\r')

if not os.path.exists('dict/ubertext_freq.csv'):
    print("Downloading ubertext_freq.csv.xz ...")
    url = 'https://lang.org.ua/static/downloads/ubertext2.0/dicts/ubertext_freq.csv.xz'
    urllib.request.urlretrieve(url, 'dict/ubertext_freq.csv.xz', reporthook=reporthook)
    print("\nDownload complete.")
    
    print("Extracting file...")
    with lzma.open('dict/ubertext_freq.csv.xz', 'rb') as f_in:
        with open('dict/ubertext_freq.csv', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("Extraction complete.")
    
    print("Removing archive...")
    os.remove('dict/ubertext_freq.csv.xz')
    print("Cleanup complete.")

def load_ignore_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        ignore_list = [line.strip() for line in file]
    print(f"Loaded {len(ignore_list)} ignore entries from {filename}")
    return ignore_list

def load_freq_dict(filename):
    freq_dict = {}
    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["pos"] == "PROPN":
                freq_dict[row["lemma"]] = row
                count += 1
    print(f"Loaded {count} PROPN entries from {filename}")
    return freq_dict

def get_word_freq(word, freq_dict):
    return freq_dict.get(word)

def freq_dict_contains(word, freq_dict):
    return word in freq_dict

def get_names_from_file(filename, ignore_list):
    with open(filename, 'r', encoding='utf-8') as file:
        names = [line.strip() for line in file if not line.startswith(' ')]
    final_names = [name.split()[0] for name in names if name not in ignore_list]
    print(f"Extracted {len(final_names)} names from {filename}")
    return final_names

def normalize_freq(freq_dict):
    try:
        print(f"Normalizing frequencies for {len(freq_dict)} items...")
        sum_freq = sum(float(freq['freq_in_corpus']) for freq in freq_dict.values())
        print(f"Total frequency sum: {sum_freq}")
        for name in freq_dict:
            freq_dict[name]['freq_in_corpus'] = float(freq_dict[name]['freq_in_corpus']) / sum_freq
        print("Normalization complete.")
        return freq_dict
    except Exception as e:
        print(f"Error normalizing frequency for {freq_dict}")
        raise e

def get_names_freq(filename, freq_dict, ignore_list):
    print(f"\nProcessing file: {filename}")
    names = get_names_from_file(filename, ignore_list)
    print(f"Loaded {len(names)} names from file {filename}")

    names_freq_dict = {}
    for i, name in enumerate(names):
        if freq_dict_contains(name, freq_dict):
            names_freq_dict[name] = get_word_freq(name, freq_dict)
    
    names_freq_dict = normalize_freq(names_freq_dict)
    print("Sorting names by frequency...")
    names_freq_dict = sorted(names_freq_dict.items(), key=lambda x: x[1]['freq_in_corpus'], reverse=True)
    print("Sorting complete.")
    return names_freq_dict

def save_names_freq_dict(names_freq_dict, filename):
    print(f"Saving frequency dictionary to {filename} with {len(names_freq_dict)} entries...")
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'freq_in_corpus'])
        writer.writeheader()
        for name in names_freq_dict:
            writer.writerow({'name': name[0], 'freq_in_corpus': name[1]['freq_in_corpus']})
    print(f"Saved frequency dictionary to {filename}.")

# Load resources
names_ignore_list = load_ignore_list('dict/ignore_list.txt')
freq_dict = load_freq_dict('dict/ubertext_freq.csv')

os.makedirs('generated', exist_ok=True)

# Process female and male first names
print("\nProcessing female first names...")
female_fname_freq_dict = get_names_freq('dict/wiki_female_fname.txt', freq_dict, names_ignore_list)
print("Processing male first names...")
male_fname_freq_dict = get_names_freq('dict/wiki_male_fname.txt', freq_dict, names_ignore_list)

save_names_freq_dict(female_fname_freq_dict, 'generated/female_fname_freq_dict.csv')
save_names_freq_dict(male_fname_freq_dict, 'generated/male_fname_freq_dict.csv')

# Process last names (ignore list includes names from first names)
print("\nProcessing last names...")
lname_ignore_list = names_ignore_list + [name[0] for name in female_fname_freq_dict] + [name[0] for name in male_fname_freq_dict]
lname_freq_dict = get_names_freq('dict/wiki_lname.txt', freq_dict, lname_ignore_list)
save_names_freq_dict(lname_freq_dict, 'generated/lname_freq_dict.csv')

# Patronymics
print("\nProcessing female patronymics...")
female_pname_freq_dict = get_names_freq('dict/vesum_female_pname.txt', freq_dict, [])
print("Processing male patronymics...")
male_pname_freq_dict = get_names_freq('dict/vesum_male_pname.txt', freq_dict, [])
save_names_freq_dict(female_pname_freq_dict, 'generated/female_pname_freq_dict.csv')
save_names_freq_dict(male_pname_freq_dict, 'generated/male_pname_freq_dict.csv')
