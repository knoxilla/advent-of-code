#!/usr/bin/env python3

with open("forest", "r") as f:
    pattern = f.read().splitlines()

# for some visual fun
print_track = False

# our modulo for loopin' 'round the pattern lines
pattern_width = len(pattern[0])


def count_the_trees(horizontal, vertical):
    to_the_side = horizontal
    downwards = vertical

    # start one move into the tobogganing
    startfile = horizontal

    # initialize
    rank = 0
    trees = 0

    if print_track:
        print(pattern[rank])

    # proceed sidewise and rankwise
    for pos in range(startfile, to_the_side * len(pattern), to_the_side):
        # rank where we will be checking for a tree
        rank += downwards

        # this is the most obscure nonsense here
        # i am not proud of myself
        if rank >= len(pattern) - (downwards - 1):
            break

        over = pos % pattern_width

        # just so we can replace chars easily
        pattern_list = list(pattern[rank])

        if pattern[rank][over] == "#":
            pattern_list[over] = "X"
            # the only line that matters
            trees += 1
        else:
            pattern_list[over] = "O"

        sled_track = "".join(pattern_list)

        if print_track:
            print(rank + 1, sled_track)

    print(f">>>>>>> ({to_the_side}/{downwards}): {trees} trees encountered!")

    if print_track:
        print("")

    return trees


if __name__ == "__main__":

    trajectories = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print("And we're off!\n")

    trees_seen = []
    for t in trajectories:
        trees_seen.append(count_the_trees(*t))

    product = 1
    for trees in trees_seen:
        product *= trees

    print(f"\nMultiplied together: {product}")
