with open('class_scores.txt', 'r') as f1, open('new_scores.txt', 'w') as f2:
    for i in f1:
        name, score = i.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=f2)
