

def first_fit(item_list, bin_size):
    # Initialise a list of bins
    bin_list = [0]

    for item in item_list:
        # Try to fit the item in the existing bins
        fit_found = False
        for i in range(len(bin_list)):
            if item <= bin_size - bin_list[i]:
                bin_list[i] += item
                fit_found = True
                break

        # If the item didn't fit in any existing bin, create a new bin
        if not fit_found:
            bin_list.append(item)

    return bin_list

# Data we have:
# size of each item
item_list = [2, 1, 3, 2, 1, 2, 3, 1]

# size of bin
bin_size = 4

# Output:
# some list of bins with what each bin contains.
# Solution to the question "how many bins are needed"
# can be obtained from len(bin_list).

print(first_fit(item_list, bin_size) == [4, 4, 4, 3])


