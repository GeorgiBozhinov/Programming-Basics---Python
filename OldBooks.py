searched_book = input()
book_capacity = int(input())

counter = -1

while book_capacity > 0:
    book = input()
    counter += 1
    book_capacity -= 1

    if searched_book == book:
        print("You checked %d books and found it." % counter)
        break

if book_capacity == 0:
    print("The book you search is not here!")
    print("You checked %d books." % counter)