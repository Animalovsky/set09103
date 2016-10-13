from  flask  import  Flask , render_template, jsonify, json
app = Flask(__name__)

# This route will return a list in JSON format
@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1993', 'img': 'http://www.themasterdiskrecord.com/wp-content/uploads/2014/08/Nirvana-Nevermind-cover-300x300.jpeg'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://e.snmc.io/lk/f/l/6b09725acea3aefbafbf503a76885d0c/1612455.jpg'},
        {'artist_name': 'System of a Down', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'http://loudwire.com/files/2015/09/System-of-a-Down-Toxicity.png'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://loudwire.com/files/2014/01/Life-is-Peachy.jpg'}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return render_template("index.html", results=list)

@app.route('/<artist_name>/')
def artist(artist_name):
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1993', 'img': 'https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://e.snmc.io/lk/f/l/6b09725acea3aefbafbf503a76885d0c/1612455.jpg'},
		{'artist_name': 'System of a Down', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'http://loudwire.com/files/2015/09/System-of-a-Down-Toxicity.png'},
		{'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://loudwire.com/files/2014/01/Life-is-Peachy.jpg'}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return render_template("artist.html", results=list, art=artist_name)	
	
@app.route('/<artist_name>/<album_name>/')
def album(artist_name, album_name):
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1993', 'img': 'https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://e.snmc.io/lk/f/l/6b09725acea3aefbafbf503a76885d0c/1612455.jpg'},
		{'artist_name': 'System_of_a_Down', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'http://loudwire.com/files/2015/09/System-of-a-Down-Toxicity.png'},
		{'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://loudwire.com/files/2014/01/Life-is-Peachy.jpg'}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return render_template("album.html", results=list, album=album_name)



if __name__  == "__main__":
    app.run(host='0.0.0.0 ', debug=True)