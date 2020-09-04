def has_negatives(a):
    """
    YOUR CODE HERE
    """

    # okay my hasmap has a key of postive numbers and values of its
    # negavtive number counterparts

    d = {}
    result = []
    # first we need to loop throgh each number and set up the index.
    for pos_num in a:
        d[pos_num] = 1
        # check it
        if pos_num != -pos_num in d:
            # okay you can use the abs method to
            # return only the postive integer
            result.append(abs(pos_num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
