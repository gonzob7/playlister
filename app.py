from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists
app = Flask(__name__)


#MOCK ARRAY OF PROJECTS
#playlists = [
#    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
#]

@app.route('/')
def playlist_index():
    '''Show all playlists.'''
    return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def playlists_new():
    '''Create a new playlist'''
    return render_template('playlists_new.html')

if __name__ == "__main__":
    app.run(debug=True)
