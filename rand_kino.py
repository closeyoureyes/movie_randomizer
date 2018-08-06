import pandas

kinolist = pandas.read_excel("kinopoisk.xls")

def rand_kino(c, n, kinolist):
    if c.lower() == "s":
        kinolist = kinolist.loc[kinolist.loc[:,"год"].apply(str).str.match("\d{4}\s*–")]
    if c.lower() == "k":
        kinolist = kinolist.loc[kinolist.loc[:,"год"].apply(str).str.match("\d{4}$")]
    for i in range(0, n):
        r = kinolist.sample()
        if str(r.iloc[0]["оригинальное название"]) != "nan":
            print ("%d: %s (%s), %s" % (i+1, r.iloc[0]["русскоязычное название"], r.iloc[0]["оригинальное название"], r.iloc[0]["год"]))
        else:
            print ("%d: %s, %s" % (i+1, r.iloc[0]["русскоязычное название"], r.iloc[0]["год"]))

print("Куку ёпта!")
choice = input("Чё хошь, серик или кено? S is for serik, K is for Keno: ")
number = int(input("Сколько штук? "))
print (choice.lower())
if choice.lower() not in 'sk':
    print ("Жмакай правильно!")
else:
    rand_kino(choice, number, kinolist)
