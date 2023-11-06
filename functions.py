def most_frequent(input_string):
    letter_counts = {}
    for letter in input_string:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    for letter, frequency in sorted_letter_counts:
        print(f"{letter} = {frequency:02d}", end=" ")

input_string = input("Please enter a string: ")
most_frequent(input_string)
