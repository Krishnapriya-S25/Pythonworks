from json import load
f=open("C:\\Users\\pc\\Desktop\\Pythonworks\\dataset\\books.json")
data=load(f)

# for book in data:

    # print(book)

# all_titles=[book.get("title") for book in data]

# print(all_titles)

# page_filter=[book.get("title") for book in data if book.get("pages")<250]

# print(page_filter)

all_genres=[book.get("genre")for book in data ]
# print(set(all_genres))

# genre_count={genre:all_genres.count(genre)for genre in all_genres}
# print(genre_count)

#printcostly book

# costly_book=max(data,key=lambda d:d.get("price"))
# print(costly_book.get("title"))

#author with more than onebook

all_authors=[book.get("author")for book in data]
author_count={auth:all_authors.count(auth) for auth in all_authors}
print([k for k,v in author_count.items() if v>1])