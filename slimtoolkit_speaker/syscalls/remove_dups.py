
def remove_duplicates(file_path):
    unique_words = set()

    # Read the file and add each word to the set
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                unique_words.add(word)

    # Write the unique words to a new file
    with open('output.txt', 'w') as output_file:
        for word in unique_words:
            output_file.write(word + '\n')

    print('Duplicates removed. Unique words written to output.txt.')

# Specify the file path of your input text file
input_file_path = 'speaker_redis.txt'

# Call the function to remove duplicates
remove_duplicates(input_file_path)
