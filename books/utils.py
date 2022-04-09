from typing import List, Dict, Any

import requests
from logging import getLogger

from django.utils.dateparse import parse_date
from requests import RequestException, Response

from books.models import Book, BookAuthor, Category

google_logger = getLogger("GoogleLogger")


def get_books_from_google_api(query_arg: str = "*") -> List[Book]:
    print("run")
    books_volume_url = f"https://www.googleapis.com/books/v1/volumes?q={query_arg}&startIndex=0&maxResults=40"
    books: List[Book] = []
    try:
        google_response: Response = requests.get(books_volume_url)
    except RequestException as e:
        # google_logger.error(f"Encounter error while requesting to google, more: {e.args}")
        print(f"Encounter error while requesting to google, more: {e.args}")
        return []
    else:
        if 200 <= google_response.status_code < 300:
            results: Dict[str, Any] = google_response.json()
            # google_logger.info(results)
            for item in results.get("items", []):
                books.append(_build_book_from_item(item))
            print(results)
        else:
            # google_logger.error(f"Request of {google_response.url} has status = {google_response.status_code}")
            print(f"Request of {google_response.url} has status = {google_response.status_code}")
        return books


def _build_book_from_item(item: Dict[str, Any]) -> Book:
    book_info: Dict[str, Any] = item["volumeInfo"]
    # update_or_create return tuple of [Object, IsCreated] - we need only object in that case
    authors = [BookAuthor.objects.update_or_create(name=author_name)[0] for author_name in book_info.get("authors", [])]
    categories = [Category.objects.update_or_create(name=category_name)[0] for category_name in book_info.get("authors", [])]
    book = Book.objects.update_or_create(
        title=book_info.get("title"),
        publisher=book_info.get("publisher"),
        published_date=parse_date(book_info.get("publishedDate")) if book_info.get("publishedDate") else None,
        average_rating=book_info.get("averageRating")
    )[0]
    book.authors.set([author.id for author in authors])
    book.categories.set([category.id for category in categories])
    return book
