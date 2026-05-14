def solution(words):
    result = ""
    for i in range(len(words)):
        # Extracts letter form position 'i' from the word 'i'
        result += words[i][i]
    return result


print(solution(["yoda", "best", "has"]))#should return "yes"
print(solution(["cat", "dog", "fish", "Gnat"]))#should return "cost"