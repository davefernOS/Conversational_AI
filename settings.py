
def init():
	if os.path.exists("user_loc.txt"):
  		os.remove("user_loc.txt")


def edit_loc(lat, lng):
	f = open("user_loc.txt", "w")
	f.write("{}:{}".format(lat,lng))
	f.close()

def get_loc():
	f = open("user_loc.txt", "r")
	location = f.readline()
	location = location.split(':')
	return location

def get_db():
    """Open a new database connection."""
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = sqlite3.connect(
            database.sqlite3)

    return flask.g.sqlite_db