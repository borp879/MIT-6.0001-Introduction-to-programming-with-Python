# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def insert_in_all_positions(char, word_list):
    existing_list = []
    output_list = []
    for element in word_list:
        existing_list.append(list(element))
    for lst in existing_list:
        for i in range(len(lst) + 1):
            lst.insert(i, char)
            output_list.append(''.join(lst))
            lst.remove(char)
    return output_list


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return list(sequence)
    else:
        return insert_in_all_positions(sequence[0], get_permutations(sequence[1:]))











if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

