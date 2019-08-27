def likes(*arr: str) -> str:
    length = len(arr)

    if length == 0:
        return "No one like this"
    elif 0 < length < 2:
        return arr[0] + " like this"
    elif 1 < length < 3:
        return "{} and {}".format(arr[0], arr[1]) + " like this"
    elif length == 3:
        return "{}, {} and {}".format(arr[0], arr[1], arr[2]) + " like this"
    else:
        length -= 2
        return "{}, {} and {} others".format(arr[0], arr[1], length) + " like this"


if __name__ == "__main__":
    print(likes("John", "Bob", "Peter", "Matt"))
