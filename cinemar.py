import user.add
#import peli.add
import sqlite

#user.add.client("adolecente","17","adolecente2","123")
#peli.add.add("titulo", "140", 1, 2)

personas = sqlite.select("select * from PERSONAS")
print(personas)