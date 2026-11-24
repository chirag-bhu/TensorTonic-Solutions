def word_count_dict(sentences: list) -> dict:
    
    result = {}

    for sentence in sentences:
        for word in sentence:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

    return result