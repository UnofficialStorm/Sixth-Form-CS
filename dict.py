bookfilms1 = {"name" : "The life of pi","author" : "Yann Martel","cover" : "Paperback","price" : "£6.29"}
bookfilms2 = {"name" : "The Lord of the Rings","author" : "J.R.R Tolkein","cover" : "Paperback","price" : "£18.74"}
bookfilms3 = {"name" : "To kill a mockingbird","author" : "Harper Lee","cover" : "Hardcover","price" : "£12.91"}
bookfilms4 = {"name" : "The girl with the dragon tattoo","author" : "Stieg Larsson","cover" : "Kindle Edition","price" : "£4.99"}
bookfilms5 = {"name" : "Lord of the flies","author" : "William Golding","cover" : "Paperback","price" : "£5.99"}

lst = (bookfilms1, bookfilms2, bookfilms3, bookfilms4, bookfilms5)
length = len(lst)
count = 0

print("Great books turned into great films\n")
while count != length:
    for key in lst[count]:
        value = lst[count]
        print(value[key])
    print("")
    count = count + 1



