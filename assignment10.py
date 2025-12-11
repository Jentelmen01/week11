def organize_books(reading_log):
    library = {}
    for item in reading_log:
        genre, title, pages = item.split(",")
        pages = int(pages)
        if genre not in library:
            library[genre] = []
        library[genre].append((title, pages))
    return library


def print_genre_stats(library_dict):
    for genre, books in library_dict.items():
        total = 0
        for title, pages in books:
            total += pages
        print(f"{genre}: {total} pages total")



reading_log = [
    "Fantasy,The Hobbit,310",
    "SciFi,Dune,412",
    "Fantasy,Harry Potter,223",
    "Mystery,Sherlock Holmes,300",
    "SciFi,Ender's Game,324",
    "Fantasy,The Alchemist,160"
]
library_dict = organize_books(reading_log)
print_genre_stats(library_dict)









