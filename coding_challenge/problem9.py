if __name__ == '__main__':
    name_list={}
    for _ in range(int(input())):
        name = input("Enter name: ")
        name_list[name] = float(input("Enter score: "))
    
    unique_scores = sorted(set(name_list.values()))
    
    second_lowest_score = unique_scores[1]

    print(second_lowest_score)

    min_names = [name for name, score in name_list.items() if score == second_lowest_score]
    min_names.sort()  # Sort the names alphabetically
    
    for name in min_names:
        print(name)