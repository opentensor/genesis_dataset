def clean_file(filename):
    file = open(filename, 'rt')
    text = file.read()
    file.close()

    # Split into words by white space
    words = text.split()

    # Convert to lower case
    words = [word.lower() for word in words]
    print(words[:100])