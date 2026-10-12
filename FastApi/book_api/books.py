from fastapi import APIRouter,HTTPException,Query
from pydantic import BaseModel
router = APIRouter()

books = []
next_id = 1


@router.get("/books")
def get_books(
    limit  : int = Query(default = 10, ge = 1, le = 100),
    off_set : int = Query(default = 0,ge = 0)):
    return books[off_set : off_set + limit]

@router.get("/books/{book_id}")
def get_book(book_id : int ):
    for book in books:
        if book.id == book_id:
            return book
        
    raise HTTPException(
        status_code = 404,
        detail = "No Book record Found",
            )

class CreateBook(BaseModel):
    author : str
    title : str
    pages : int

class Book(BaseModel):
    id : int 
    author : str
    title : str
    pages : int


@router.post("/book")
def create_book(book:CreateBook):
    global next_id
    new_book = Book(
        id = next_id,
        author = book.author,
        title =  book.title,
        pages = book.pages
    )
    books.append(new_book)
    next_id += 1 
    return new_book