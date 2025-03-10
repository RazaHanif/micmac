def main():
    print("How many classes do you want to average?")
    total = get_num("Classes")

    print(get_scores(total))


def get_num(str):
    while True:
        try:
            n = int(input(f"{str}: "))
        except (ValueError):
            pass
        else:
            if n > 0:
                return n

def get_scores(num):
    scores = []
    for i in range(num):
        print(f"Enter Score {i + 1}")
        score = get_num("Score")
        scores.append(score)

    average = sum(scores) / len(scores)
    return f"Average score for {num} scores: {average}"

main()