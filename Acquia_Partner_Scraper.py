try:
    from googlesearch import search
except ImportError: 
    print("No module named 'googlesearch' found")

# to search
#query = "Geeksforgeeks"
query = "site://https://www.acquia.com/partners/showcase/"
 
for j in search(query, tld="co.in", num=10, stop=1, pause=2.0):
#for j in search(query, tld="com", num=10, stop=None, pause=2.0):
    print(j)

