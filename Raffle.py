import csv
import random
import sys

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            entries = []
            csv_reader = csv.reader(file)
            for row in csv_reader:
                entries.append(row)
            return entries
    except FileNotFoundError:
        print("file not found ):")
    except Exception as e:
        print("some other error")

def sum_money(entries):
    total = 0
    index = 0
    for entry in entries:
        if index != 0:
            cost = entry[2].split(' ')
            num = cost[2][1:]
            total += int(num)
        index += 1
    return total


def create_dict(entries):
    diction = {}
    index = 0
    for entry in entries:
        num = entry[2].split(' ')
        if index != 0:
            diction[entry[1]] = int(num[0])
        index += 1
    return diction

def raffle_list(dict):
    final = []
    for person in dict:
        for _ in range(dict[person]):
            final.append(person)
    return final

def select5(final):
    random.shuffle(final)
    return final[:5]

def main(args):
    first = read_file(args)
    diction = create_dict(first)
    raffle = raffle_list(diction)
    total = sum_money(first)
    print(select5(raffle))
    print(total)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("argument issue")