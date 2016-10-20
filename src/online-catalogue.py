from  flask  import  Flask , render_template, jsonify, json, url_for
import os
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
    artist = [
        {'artist_name': 'Nirvana', 'img': 'http://localhost:5000/static/images/nirvana-top.png', 'bio': "Nirvana was an American alternative rock band. They were one of the most successful and influential bands of that time. Since they formed, they have sold over 75 million records all over the world. They played a style of rock music known as grunge, which was highly influenced by 1980s alternative rock, 1970s punk, and heavy metal. Grunge became more commercially successful than the previous punk rock, as promoted to the world by Sub Pop Records. Nirvana greatly affected the style of other grunge bands such as Pearl Jam, Soundgarden, and Alice in Chains. They split up after their lead singer Kurt Cobain died in 1994 after he committed suicide. On April 10, 2014, Nirvana received a star in the Rock and Roll Hall of Fame."},
        {'artist_name': 'Eminem', 'img': 'http://localhost:5000/static/images/eminem-top2.png', 'bio': "To call Eminem hip-hop's Elvis is correct to a degree, but it's largely inaccurate. Certainly, Eminem was the first white rapper since the 'Beastie Boys' to garner both sales and critical respect, but his impact exceeded this confining distinction. On sheer verbal skills, Eminem was one of the greatest MCs of his generation rapid, fluid, dexterous, and unpredictable, as withering aside and thanks to his mentor Dr. Dre, he had music to match thick, muscular loops that evoked the terror and paraoia Em's music conjured."},
        {'artist_name': 'Adele', 'img': 'http://localhost:5000/static/images/adele-top.png', 'bio': "When the U.K. press began dubbing Adele the next Amy Winehouse in late 2007, the hype didn't touch upon the singer/songwriter influence found in the Londoner's music. Influenced by Roberta Flack and Suzanne Vega as much as Jill Scott, Adele soon became a phenomenon in her own right her second album, 21, eventually sold an estimated 30 million copies worldwide, making her one of the few sales successes in an age of digital streaming."},
        {'artist_name': 'Korn', 'img': 'http://localhost:5000/static/images/korn-top.png', 'bio': "Korn (sometimes written as KoRn with reversed 'R' to fit their logo) is a Grammy Award-winning band from Bakersfield, California. People often say they created the nu metal genre. Along with other bands of the time, they were influences for a wave of nu metal, alternative metal and rap metal bands through the mid 1990s and early 2000s, helping Limp Bizkit (who were discovered by Korn themselves) and Slipknot more than other bands. Despite this, Korn have been quoted for disliking the term and even being called 'metal'. Jonathan Davis has said that Korn's music can not be classified and that it contains many other influences besides simply 'metal'. The official review on the iTunes Store for their first album goes as far as saying that Korn 'hate the term'. Their first album was first sold in 1994 and also called KoRn. Since then, Korn has sold over 35 millions records worldwide - including 16,5 millions in the U.S., making them one of the best-selling metal acts of the last twelve years."},
		{'artist_name': 'Michael Jackson', 'img': 'http://localhost:5000/static/images/mj-top.png', 'bio': "Michael Joseph Jackson (August 29, 1958 to June 25, 2009) was an American singer, songwriter, record producer, dancer, and actor. Called the King of Pop, his contributions to music, dance, and fashion along with his publicized personal life made him a global figure in popular culture for over four decades. The eighth child of the Jackson family (one of whom died in infancy), Michael made his professional debut in 1964 with his elder brothers Jackie, Tito, Jermaine, and Marlon as a member of the Jackson 5. He began his solo career in 1971. In the early 1980s, Jackson became a dominant figure in popular music. His music videos, including those of Beat It, Billie Jean, and Thriller from his 1982 album Thriller, are credited with breaking racial barriers and transforming the medium into an art form and promotional tool. The popularity of these videos helped bring the television channel MTV to fame. Jackson's 1987 album Bad spawned the U.S. Billboard Hot 100 number-one singles I Just Can't Stop Loving You, Bad, The Way You Make Me Feel, Man in the Mirror, and Dirty Diana, becoming the first album to have five number-one singles on the Billboard Hot 100. He continued to innovate with videos such as Black or White and Scream throughout the 1990s, and forged a reputation as a touring solo artist. Through stage and video performances, Jackson popularized a number of complicated dance techniques, such as the robot and the moonwalk, to which he gave the name. His distinctive sound and style has influenced numerous artists of various music genres."},
		{'artist_name': 'Kendrick Lamar', 'img': 'http://localhost:5000/static/images/kl-top.png', 'bio': "Kendrick Lamar Duckworth, who performs as Kendrick Lamar, was born in Compton, California, on June 17, 1987. After writing stories as a child, he put to music some lyrics about the rough Compton streets he grew up on. He rapped under the name K-Dot, releasing a series of increasingly popular mix tapes, which brought him to the attention of hip-hop super-producer Dr. Dre. Lamar's debut major-label recording, good kid, m.A.A.d City, was released to great acclaim and impressive sales for an up-and-coming recording artist. He continued to receive an array of accolades for his 2015 Grammy-winning album To Pimp a Butterfly."}
    ]
    albums = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1991', 'img': 'http://localhost:5000/static/images/nirvana_nvm.jpeg', 'genre': 'rock'},
		{'artist_name': 'Nirvana', 'album_name': 'In Utero', 'date_of_release': '1993', 'img': 'http://localhost:5000/static/images/nirvana_inutero.jpg', 'genre': 'rock'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://localhost:5000/static/images/eminem_mmlp.jpg', 'genre': 'rap'},
		{'artist_name': 'Eminem', 'album_name': 'Relapse', 'date_of_release': '2009', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rap'},
		{'artist_name': 'Adele', 'album_name': '21', 'date_of_release': '2011', 'img': 'http://localhost:5000/static/images/adele_21.jpg', 'genre': 'pop'},
		{'artist_name': 'Adele', 'album_name': '25', 'date_of_release': '2015', 'img': 'http://localhost:5000/static/images/adele_25.png', 'genre': 'pop'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://localhost:5000/static/images/korn_lip.jpg', 'genre': 'rock'},
		{'artist_name': 'Korn', 'album_name': 'Follow the Leader', 'date_of_release': '1998', 'img': 'http://localhost:5000/static/images/korn_ftl.jpg', 'genre': 'rock'},
		{'artist_name': 'Michael Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'http://localhost:5000/static/images/mj_thriller.png', 'genre': 'pop'},
        {'artist_name': 'Michael Jackson', 'album_name': 'Bad', 'date_of_release': '1987', 'img': 'http://localhost:5000/static/images/mj_bad.png', 'genre': 'pop'},
		{'artist_name': 'Kendrick Lamar', 'album_name': 'Good kid, M.A.A.D City', 'date_of_release': '2012', 'img': 'http://localhost:5000/static/images/kl_goodkid.jpg', 'genre': 'rap'},
        {'artist_name': 'Kendrick Lamar', 'album_name': 'How to pimp a butterfly', 'date_of_release': '2015', 'img': 'http://localhost:5000/static/images/kl_htpab.png', 'genre': 'rap'}
    ]
    return render_template("artist.html", artist=artist, albums=albums, artist_name=artist_name)

# This is all the albums route.	
@app.route('/all_artists/albums/')
def albums():
    albums = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1991', 'img': 'http://localhost:5000/static/images/nirvana_nvm.jpeg', 'genre': 'rock'},
		{'artist_name': 'Nirvana', 'album_name': 'In Utero', 'date_of_release': '1993', 'img': 'http://localhost:5000/static/images/nirvana_inutero.jpg', 'genre': 'rock'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://localhost:5000/static/images/eminem_mmlp.jpg', 'genre': 'rap'},
		{'artist_name': 'Eminem', 'album_name': 'Relapse', 'date_of_release': '2009', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rap'},
		{'artist_name': 'Adele', 'album_name': '21', 'date_of_release': '2011', 'img': 'http://localhost:5000/static/images/adele_21.jpg', 'genre': 'pop'},
		{'artist_name': 'Adele', 'album_name': '25', 'date_of_release': '2015', 'img': 'http://localhost:5000/static/images/adele_25.png', 'genre': 'pop'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://localhost:5000/static/images/korn_lip.jpg', 'genre': 'rock'},
		{'artist_name': 'Korn', 'album_name': 'Follow the Leader', 'date_of_release': '1998', 'img': 'http://localhost:5000/static/images/korn_ftl.jpg', 'genre': 'rock'},
		{'artist_name': 'Michael Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'http://localhost:5000/static/images/mj_thriller.png', 'genre': 'pop'},
        {'artist_name': 'Michael Jackson', 'album_name': 'Bad', 'date_of_release': '1987', 'img': 'http://localhost:5000/static/images/mj_bad.png', 'genre': 'pop'},
		{'artist_name': 'Kendrick Lamar', 'album_name': 'Good kid, M.A.A.D City', 'date_of_release': '2012', 'img': 'http://localhost:5000/static/images/kl_goodkid.jpg', 'genre': 'rap'},
        {'artist_name': 'Kendrick Lamar', 'album_name': 'How to pimp a butterfly', 'date_of_release': '2015', 'img': 'http://localhost:5000/static/images/kl_htpab.png', 'genre': 'rap'}
    ]
    return render_template("albums.html", results=albums)
	
	# This is all the albums route.	
@app.route('/<artist_name>/<album_name>/')
def album(album_name, artist_name):
    album = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': 'September 24, 1991', 'img': 'http://localhost:5000/static/images/nirvana_nvm.jpeg', 'genre': 'rock', 'studio': 'DGC Records'},
		{'artist_name': 'Nirvana', 'album_name': 'In Utero', 'date_of_release': 'September 21, 1993', 'img': 'http://localhost:5000/static/images/nirvana_inutero.jpg', 'genre': 'rock', 'studio': 'DGC Records'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': 'May 23, 2000', 'img': 'http://localhost:5000/static/images/eminem_mmlp.jpg', 'genre': 'rap', 'studio': 'Aftermath Entertainment, Interscope Records and Shady Records'},
		{'artist_name': 'Eminem', 'album_name': 'Relapse', 'date_of_release': 'May 15, 2009', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rap', 'studio': 'Aftermath Entertainment, Interscope Records and Shady Records'},
		{'artist_name': 'Adele', 'album_name': '21', 'date_of_release': 'January 24, 2011', 'img': 'http://localhost:5000/static/images/adele_21.jpg', 'genre': 'pop', 'studio': 'XL and Columbia'},
		{'artist_name': 'Adele', 'album_name': '25', 'date_of_release': '20 November 2015', 'img': 'http://localhost:5000/static/images/adele_25.png', 'genre': 'pop', 'studio': 'XL and Columbia'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': 'October 15, 1996', 'img': 'http://localhost:5000/static/images/korn_lip.jpg', 'genre': 'rock', 'studio': 'Epic Records'},
		{'artist_name': 'Korn', 'album_name': 'Follow the Leader', 'date_of_release': 'August 18, 1998', 'img': 'http://localhost:5000/static/images/korn_ftl.jpg', 'genre': 'rock', 'studio': 'Epic/Immortal Records'},
		{'artist_name': 'Michael Jackson', 'album_name': 'Thriller', 'date_of_release': 'November 30, 1982', 'img': 'http://localhost:5000/static/images/mj_thriller.png', 'genre': 'pop', 'studio': 'Epic Records'},
        {'artist_name': 'Michael Jackson', 'album_name': 'Bad', 'date_of_release': 'August 31, 1987', 'img': 'http://localhost:5000/static/images/mj_bad.png', 'genre': 'pop', 'studio': 'Epic Records'},
		{'artist_name': 'Kendrick Lamar', 'album_name': 'Good kid, M.A.A.D City', 'date_of_release': 'October 22, 2012', 'img': 'http://localhost:5000/static/images/kl_goodkid.jpg', 'genre': 'rap', 'studio': 'TDE, Aftermath Entertainment and Interscope Records'},
        {'artist_name': 'Kendrick Lamar', 'album_name': 'How to pimp a butterfly', 'date_of_release': 'March 15, 2015', 'img': 'http://localhost:5000/static/images/kl_htpab.png', 'genre': 'rap', 'studio': 'TDE, Aftermath Entertainment and Interscope Records'}
    ]
    tracks = [
	    {'album_name': 'Nevermind', 1: 'Smells like teen spirit', 2: 'In Bloom', 3: 'Come as you are', 4: 'Breed', 5: 'Lithium', 6: 'Polly', 7: 'Territorial Pissings', 8: 'Drain You', 9: 'Lounge act', 10: 'Stay away', 11: 'On a plain', 12: 'Something in the way'},
		{'album_name': 'Relapse', 1: 'Hello', 2: '3AM',},
	]
    return render_template("album.html", album=album, album_name=album_name, artist_name=artist_name, tracks=tracks)
	
# This is all the albums route.	
@app.route('/genres/')
def genres():
    albums = [
		{'genre': 'pop'},
		{'genre': 'rock'},
        {'genre': 'rap'},
    ]
    return render_template("genres.html", results=albums, genre=genre)	
	
	
# This is all the albums route.	
@app.route('/genres/<genre>/')
def genre(genre):
    albums = [
        {'artist_name': 'Nirvana', 'album_name': 'Nevermind', 'date_of_release': '1991', 'img': 'http://localhost:5000/static/images/nirvana_nvm.jpeg', 'genre': 'rock'},
		{'artist_name': 'Nirvana', 'album_name': 'In Utero', 'date_of_release': '1993', 'img': 'http://localhost:5000/static/images/nirvana_inutero.jpg', 'genre': 'rock'},
        {'artist_name': 'Eminem', 'album_name': 'Marshal Mathers LP', 'date_of_release': '2000', 'img': 'http://localhost:5000/static/images/eminem_mmlp.jpg', 'genre': 'rap'},
		{'artist_name': 'Eminem', 'album_name': 'Relapse', 'date_of_release': '2009', 'img': 'http://localhost:5000/static/images/eminem_relapse.jpg', 'genre': 'rap'},
		{'artist_name': 'Adele', 'album_name': '21', 'date_of_release': '2011', 'img': 'http://localhost:5000/static/images/adele_21.jpg', 'genre': 'pop'},
		{'artist_name': 'Adele', 'album_name': '25', 'date_of_release': '2015', 'img': 'http://localhost:5000/static/images/adele_25.png', 'genre': 'pop'},
        {'artist_name': 'Korn', 'album_name': 'Life is Peachy', 'date_of_release': '1996', 'img': 'http://localhost:5000/static/images/korn_lip.jpg', 'genre': 'rock'},
		{'artist_name': 'Korn', 'album_name': 'Follow the Leader', 'date_of_release': '1998', 'img': 'http://localhost:5000/static/images/korn_ftl.jpg', 'genre': 'rock'},
		{'artist_name': 'Michael Jackson', 'album_name': 'Thriller', 'date_of_release': '1982', 'img': 'http://localhost:5000/static/images/mj_thriller.png', 'genre': 'pop'},
        {'artist_name': 'Michael Jackson', 'album_name': 'Bad', 'date_of_release': '1987', 'img': 'http://localhost:5000/static/images/mj_bad.png', 'genre': 'pop'},
		{'artist_name': 'Kendrick Lamar', 'album_name': 'Good kid, M.A.A.D City', 'date_of_release': '2012', 'img': 'http://localhost:5000/static/images/kl_goodkid.jpg', 'genre': 'rap'},
        {'artist_name': 'Kendrick Lamar', 'album_name': 'How to pimp a butterfly', 'date_of_release': '2015', 'img': 'http://localhost:5000/static/images/kl_htpab.png', 'genre': 'rap'}
    ]
    return render_template("genre.html", results=albums, genre=genre)	
	
	
if __name__  == "__main__":
	app.run(host='0.0.0.0 ', debug=True)