if __name__ == '__main__':
    N = int(input())
    commands = []
    for _ in range(N):
        commands.append(input().split())

    new_list = []
    for command in commands:
        if command[0] == 'insert':
            new_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(new_list)
        elif command[0] == 'remove':
            new_list.remove(int(command[1]))
        elif command[0] == 'append':
            new_list.append(int(command[1]))
        elif command[0] == 'sort':
            new_list.sort()
        elif command[0] == 'pop':
            new_list.pop()
        elif command[0] == 'reverse':
            new_list.reverse()