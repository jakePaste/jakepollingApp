import sqlite3 as lite


# Functionality Part

class DatabaseManage(object):

	# constructor
	def __init__(self):
		global con
		try:
			con = lite.connect("dataset.db")
			with con:
				cur = con.cursor()
				cur.execute("CREATE TABLE IF NOT EXISTS data(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1, tags TEXT)")
		except Exception:
			print("Unable to connect to DB!")

	# create data
	def insert_data(self, data):
		try:
			with con:
				cur = con.cursor()
				cur.execute(
					"INSERT INTO data(name, description, price, is_private, tags) VALUES (?,?,?,?, ?)", data
					)
				return True
		except Exception:
			return False

	# read data
	def fetch_data(self):
		try:
			with con:
				cur = con.cursor()
				cur.execute("SELECT * FROM data")
				return cur.fetchall()
		except Exception:
			return False

	# delete data
	def delete_data(self, id):
		try:
			with con:
				cur = con.cursor()
				sql = "DELETE FROM data WHERE id = ?"
				cur.execute(sql, [id])
				return True
		except Exception:
			return False


# Interface to User

def main():
	print("*"*40)
	print("\n       :: PYTHON MINI PROJECT ::\n")
	print("*"*40)

	print("\n           :: USER MENU ::\n")
	print("*"*40)

	print("\nPRESS 1. Insert a new entry \n")
	print("PRESS 2. Show all entries \n")
	print("PRESS 3. Delete entry (NEED ID OF ENTRY)\n")
	print("PRESS q. To Quit\n")

	print("*"*40)

	db = DatabaseManage()
	choice = ""

	while choice != "q":

		choice = input("\nEnter a choice: ")

		if choice == "1":
			name = input("\n Enter Name: ")
			description = input("\n Enter description: ")
			price = input("\n Enter price: ")
			private = input("\n Enter Private or Public(0/1): ")
			tags = input("\n Enter Tags(Comma Seprated): ")

			if db.insert_data([name, description, price, private, tags]):
				print("\n ***Entry was Inserted Successfully")
			else:
				print("\n ***OOPS Something goes wrong")

		elif choice == "2":
			print("\n:: Entries List ::\n")

			for index, item in enumerate (db.fetch_data()):
				print("ID : " + str(item[0]))
				print("Name : " + str(item[1]))
				print("Description : " + str(item[2]))
				print("Price : " + str(item[3]))
				private = "Yes" if item[4] else "No"
				print("Is Private : " + private)
				tags = item[5].split(",")
				print("Tags : ")
				for tag in tags:
					print("  " + tag.strip())
				print("\n")

		elif choice == "3":
			record_id = input("Enter the Id: ")

			if(db.delete_data(record_id)):
				print("\n ***Entry is Deleted Successfully")
			else:
				print("\n ***OOPS Something goes wrong")

		elif choice == "q":
			print("\n ***Successfully Terminated")

		else:
			print("\n ***BAD CHOICE")


# Starting Point

if __name__ == '__main__':
	main()