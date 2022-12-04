#!/usr/bin/env python3

def total_elf_inv(elf):
    calories = 0
    for item in elf:
        calories = calories + int(item)
    return calories

def read_file(file_path):
    elf_inv = [] ## store elf inventory
    elves = [] ## store all the elves

    f = open(file_path, "r")
    for elf in f:

        if len(elf) == 1:
            # clear elf inf
            elves.append(elf_inv)
            elf_inv=[]
        else:
            elf = elf \
                .replace("\r","") \
                .replace("\n","")
            elf_inv.append(elf)
    f.close()
    return elves


def main():
    elves_inv = []
    highest_cal = 0
    elves = read_file('./input')
    print(f"there are {len(elves)} elves")

    for elf in elves:
        if (total_elf_inv(elf) > highest_cal):
            highest_cal = total_elf_inv(elf)
        elves_inv.append(total_elf_inv(elf))
        #print(f"{total_elf_inv(elf)}")
    print(f"the highest calories was {highest_cal}")

    elves_inv.sort(reverse=True)
    for elf in elves_inv:
        print(elf)
    #print(elves_inv)
    print(f"the top 3 were totalled {elves_inv[0] + elves_inv[1] + elves_inv[2]} {elves_inv[0]}, {elves_inv[1]}, {elves_inv[2]}")


if (__name__ == "__main__"):
    main()
