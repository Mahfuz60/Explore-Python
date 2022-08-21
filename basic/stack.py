# fist in last out
books=[]
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
books.append("Learn Javascript")
books.append("Learn Python")
print(books)


# delete the last books
books.pop()
print(books)
print("Now Top books is:",books[-1])

# books empty error handle
# if not books:
#     print("No Books here in this list")