def cal(n):
    if n < 0:
      return[]

    recaman = [0]
    storage = {0}

    for k in range(1,n):
        last_number = recaman[k-1]
        next_number = last_number - k

        if next_number > 0:
            recaman.append(next_number)
        else:
            next_number = last_number + k
            recaman.append(next_number)
        storage.add(next_number)
    return recaman

length = int(input("Please enter the length:"))
final = cal(length)
print(final)