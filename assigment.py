books=[]
def add_book(books):
  book_id=input("Enter Book ID;")
  title=input("Enter Book Title")
  author=input("Enter Author Name")
  Quantity=int(input("Enter Quantity:"))
  book={"id":book_id,
        "title":title,
        "author":author,
        "quantity":quantity,}
  books.append(book)
  print("Book added sucessfully!")
  def show books():
    if len(books)==0:
      print("no books avaliable")
    else:
      for book in books :
        print()
