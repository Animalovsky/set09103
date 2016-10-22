from  flask  import  Flask , render_template, jsonify, json, url_for
app = Flask(__name__)

# This is an index route.
@app.route('/')
def index():
    json_data=open('static/data.json').read()
    data= json.loads(json_data)
    return render_template("index.html", results=data)

# This is an artist route.
@app.route('/<artist_name>/')
def artist(artist_name):
    json_data=open('static/data.json').read()
    artist= json.loads(json_data)
    json_data=open('static/albums.json').read()
    albums= json.loads(json_data)
    return render_template("artist.html", albums=albums, artist_name=artist_name, artist=artist)

# This is all the albums route.	
@app.route('/albums/')
def albums():
    json_data=open('static/albums.json').read()
    albums= json.loads(json_data)
    return render_template("albums.html", results=albums)
	
# This is the single albums route.	
@app.route('/<artist_name>/<album_name>/')
def album(album_name, artist_name):
    json_data=open('static/albums.json').read()
    albums= json.loads(json_data)
    json_data=open('static/tracks.json').read()
    tracks= json.loads(json_data)
    return render_template("album.html", albums=albums, album_name=album_name, artist_name=artist_name, tracks=tracks)
	
# This is all the genres route.	
@app.route('/genres/')
def genres():
    return render_template("genres.html")	
	
	
# This is a single genre route.	
@app.route('/genres/<genre>/')
def genre(genre):
    json_data=open('static/albums.json').read()
    albums= json.loads(json_data)
    return render_template("genre.html", results=albums, genre=genre)	
		
if __name__  == "__main__":
	app.run(host='0.0.0.0 ', debug=True)