from  flask  import  Flask , render_template, jsonify, json
app = Flask(__name__)

# This route will return a list in JSON format
@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    artists = [
        {'artist_name': 'Nirvana', 'img': 'static/images/nirvana.png', 'genre': 'rock'},
        {'artist_name': 'Eminem', 'img': 'static/images/eminem.png', 'genre': 'rap'},
        {'artist_name': 'Adele', 'img': 'static/images/adele.png', 'genre': 'pop'},
        {'artist_name': 'Korn', 'img': 'static/images/korn.png', 'genre': 'rock'},
		{'artist_name': 'Michael_Jackson', 'img': 'static/images/mj.png', 'genre': 'pop'},
		{'artist_name': 'Kendrick_Lamar', 'img': 'static/images/kl.png', 'genre': 'rap'}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return render_template("index.html", results=artists)

@app.route('/<artist_name>/')
def artist(artist_name):
    artist = [
        {'artist_name': 'Nirvana', 'img': 'http://localhost:5000/static/images/nirvana-top.png', 'bio': 'Mauris egestas arcu mi, vehicula tristique neque congue aliquam. Duis sodales nibh magna, vitae dapibus sem hendrerit at. Fusce imperdiet leo massa, et facilisis augue venenatis aliquam. Nam et volutpat felis, eget tincidunt enim. Nunc porta interdum tristique. Curabitur euismod mattis enim, pulvinar luctus eros facilisis et. Aliquam erat volutpat. Cras nisi ante, pellentesque quis sagittis at, finibus vulputate est. Duis sed justo eu odio sagittis gravida. Nam dapibus tempus odio vehicula sodales. Nam id convallis ex, vel eleifend justo. Etiam vel ullamcorper nibh, et finibus ligula. Fusce feugiat, ligula nec hendrerit interdum, tortor magna pulvinar est, a scelerisque nisl turpis a nulla.'},
        {'artist_name': 'Eminem', 'img': 'http://localhost:5000/static/images/eminem-top2.png', 'bio': 'Mauris egestas arcu mi, vehicula tristique neque congue aliquam. Duis sodales nibh magna, vitae dapibus sem hendrerit at. Fusce imperdiet leo massa, et facilisis augue venenatis aliquam. Nam et volutpat felis, eget tincidunt enim. Nunc porta interdum tristique. Curabitur euismod mattis enim, pulvinar luctus eros facilisis et. Aliquam erat volutpat. Cras nisi ante, pellentesque quis sagittis at, finibus vulputate est. Duis sed justo eu odio sagittis gravida. Nam dapibus tempus odio vehicula sodales. Nam id convallis ex, vel eleifend justo. Etiam vel ullamcorper nibh, et finibus ligula. Fusce feugiat, ligula nec hendrerit interdum, tortor magna pulvinar est, a scelerisque nisl turpis a nulla.'},
        {'artist_name': 'Adele', 'img': 'http://localhost:5000/static/images/adele-top.png', 'bio': 'Mauris egestas arcu mi, vehicula tristique neque congue aliquam. Duis sodales nibh magna, vitae dapibus sem hendrerit at. Fusce imperdiet leo massa, et facilisis augue venenatis aliquam. Nam et volutpat felis, eget tincidunt enim. Nunc porta interdum tristique. Curabitur euismod mattis enim, pulvinar luctus eros facilisis et. Aliquam erat volutpat. Cras nisi ante, pellentesque quis sagittis at, finibus vulputate est. Duis sed justo eu odio sagittis gravida. Nam dapibus tempus odio vehicula sodales. Nam id convallis ex, vel eleifend justo. Etiam vel ullamcorper nibh, et finibus ligula. Fusce feugiat, ligula nec hendrerit interdum, tortor magna pulvinar est, a scelerisque nisl turpis a nulla.'},
        {'artist_name': 'Korn', 'img': 'http://localhost:5000/static/images/korn-top.png', 'bio': 'Mauris egestas arcu mi, vehicula tristique neque congue aliquam. Duis sodales nibh magna, vitae dapibus sem hendrerit at. Fusce imperdiet leo massa, et facilisis augue venenatis aliquam. Nam et volutpat felis, eget tincidunt enim. Nunc porta interdum tristique. Curabitur euismod mattis enim, pulvinar luctus eros facilisis et. Aliquam erat volutpat. Cras nisi ante, pellentesque quis sagittis at, finibus vulputate est. Duis sed justo eu odio sagittis gravida. Nam dapibus tempus odio vehicula sodales. Nam id convallis ex, vel eleifend justo. Etiam vel ullamcorper nibh, et finibus ligula. Fusce feugiat, ligula nec hendrerit interdum, tortor magna pulvinar est, a scelerisque nisl turpis a nulla.'},
		{'artist_name': 'Michael_Jackson', 'img': 'http://localhost:5000/static/images/mj-top.png', 'bio': 'Mauris egestas arcu mi, vehicula tristique neque congue aliquam. Duis sodales nibh magna, vitae dapibus sem hendrerit at. Fusce imperdiet leo massa, et facilisis augue venenatis aliquam. Nam et volutpat felis, eget tincidunt enim. Nunc porta interdum tristique. Curabitur euismod mattis enim, pulvinar luctus eros facilisis et. Aliquam erat volutpat. Cras nisi ante, pellentesque quis sagittis at, finibus vulputate est. Duis sed justo eu odio sagittis gravida. Nam dapibus tempus odio vehicula sodales. Nam id convallis ex, vel eleifend justo. Etiam vel ullamcorper nibh, et finibus ligula. Fusce feugiat, ligula nec hendrerit interdum, tortor magna pulvinar est, a scelerisque nisl turpis a nulla.'},
		{'artist_name': 'Kendrick_Lamar', 'img': 'http://localhost:5000/static/images/kl-top.png', 'bio': 'Mauris egestas arcu mi, vehicula tristique neque congue aliquam. Duis sodales nibh magna, vitae dapibus sem hendrerit at. Fusce imperdiet leo massa, et facilisis augue venenatis aliquam. Nam et volutpat felis, eget tincidunt enim. Nunc porta interdum tristique. Curabitur euismod mattis enim, pulvinar luctus eros facilisis et. Aliquam erat volutpat. Cras nisi ante, pellentesque quis sagittis at, finibus vulputate est. Duis sed justo eu odio sagittis gravida. Nam dapibus tempus odio vehicula sodales. Nam id convallis ex, vel eleifend justo. Etiam vel ullamcorper nibh, et finibus ligula. Fusce feugiat, ligula nec hendrerit interdum, tortor magna pulvinar est, a scelerisque nisl turpis a nulla.'}
    ]
    albums = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1993', 'img': 'http://localhost:5000/static/images/nirvana_nvm.jpeg'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://localhost:5000/static/images/eminem_mmlp.jpg'},
        {'artist_name': 'Nirvana', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'http://localhost:5000/static/images/soad_toxicity.png'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://localhost:5000/static/images/korn_lip.jpg'},
		{'artist_name': 'Michael_Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'http://localhost:5000/static/images/mj_thriller.png'},
		{'artist_name': 'Eminem', 'album_name': 'Relapse', 'date_of_release': '2009', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rap'},
		{'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'},
        {'artist_name': 'S.O.A.D', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'},
		{'artist_name': 'Michael_Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'}
	
    return render_template("artist.html", artist=artist, albums=albums, artist_name=artist_name)	
	
@app.route('/albums/')
def albums():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    albums = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1993', 'img': 'http://localhost:5000/static/images/nirvana_nvm.jpeg'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://localhost:5000/static/images/eminem_mmlp.jpg'},
        {'artist_name': 'S.O.A.D', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'http://localhost:5000/static/images/soad_toxicity.png'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://localhost:5000/static/images/korn_lip.jpg'},
		{'artist_name': 'Michael_Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'http://localhost:5000/static/images/mj_thriller.png'},
		{'artist_name': 'Eminem', 'album_name': 'Relapse', 'date_of_release': '2009', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rap'},
		{'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'},
        {'artist_name': 'S.O.A.D', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'},
		{'artist_name': 'Michael_Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rock'},
	    {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1993', 'img': 'static/images/nirvana_nvm.jpeg', 'genre': 'rock'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'static/images/eminem_mmlp.jpg', 'genre': 'rock'},
        {'artist_name': 'S.O.A.D', 'album_name': 'Toxicity', 'date_of_release': '2001', 'img': 'static/images/soad_toxicity.png', 'genre': 'rock'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'static/images/korn_lip.jpg', 'genre': 'rock'},
		{'artist_name': 'Michael_Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'static/images/mj_thriller.png', 'genre': 'rock'}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return render_template("albums.html", results=albums)



if __name__  == "__main__":
    app.run(host='0.0.0.0 ', debug=True)