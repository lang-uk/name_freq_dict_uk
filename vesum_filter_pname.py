import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Split a dictionary file into multiple output files by gender and name type.")
parser.add_argument('input_file', type=str, help="Path to the dictionary file.")
parser.add_argument('max_words_per_file', type=int, nargs='?', default=1000, help="Maximum number of words per output file (default: 1000).")

args = parser.parse_args()
input_file = args.input_file
max_words_per_file = args.max_words_per_file

output_files = {
    'male_pname': open('male_pname.txt', 'w', encoding='utf-8'),
    'female_pname': open('female_pname.txt', 'w', encoding='utf-8'),
}

word_counts = {
    'male_pname': 0,
    'female_pname': 0,
}

current_word = []
current_gender = None
current_name_type = None

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue  # Skip empty lines

        if not line.startswith(' '):  # New word starts here
            # Write the previous word to the appropriate file if it doesn't exceed the max count
            if ':p:' in current_word:
                # Skip plural forms
                continue
            if current_word and current_gender and current_name_type:
                key = f'{current_gender}_{current_name_type}'
                if key in output_files and word_counts[key] < max_words_per_file:
                    output_files[key].writelines(current_word)
                    word_counts[key] += 1

            # Reset for the new word
            current_word = [line]
            current_gender = None
            current_name_type = None

            # Parse attributes to determine gender and name type
            tokens = line.strip().split()
            if len(tokens) >= 2:
                attributes = tokens[1].split(':')
                if 'm' in attributes:
                    current_gender = 'male'
                elif 'f' in attributes:
                    current_gender = 'female'

                if 'pname' in attributes:
                    current_name_type = 'pname'
        else:
            # Continuation of the current word's forms
            if ':p:' in line:
                # Skip plural forms
                continue
            current_word.append(line)

    # Handle the last word in the file
    if current_word and current_gender and current_name_type:
        key = f'{current_gender}_{current_name_type}'
        if key in output_files and word_counts[key] < max_words_per_file:
            output_files[key].writelines(current_word)
            word_counts[key] += 1

# Close all output files
for f in output_files.values():
    f.close()
