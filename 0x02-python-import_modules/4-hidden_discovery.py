#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden_discovery = dir(hidden_4)
    for n in range(len(hidden_discovery)):
        if hidden_discovery[n][0] != '_' and hidden_discovery[n][1] != '-':
            print(hidden_discovery[n])
