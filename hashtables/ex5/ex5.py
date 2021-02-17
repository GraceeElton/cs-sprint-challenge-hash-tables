# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []

    # loop through the files
    for v in files:
        # for each file path -- we want to split it and take the last one -- use that to create the dict
        chopped = v.split("/")
        if chopped[-1] not in d:
            d[chopped[-1]] = [v]
        else:
            d[chopped[-1]].append(v)

    for q in queries:
        if q in d:
            result += d[q]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
