Documentação Rest API Sound Words


```'/'```
<p>Principal route.<br>
Expected status code is 200, returning "hello" as string<br>
HTTP Method: GET</p>
<br>

```'/home/artists'```
<p>Return all artists registered on database.<br>
HTTP Method: GET<br>
Body as json: {"name": "name_of_artist", "genre": "genre_of_artist"}</p>
<br>

```'/home/musics'```
<p>Return all musics already registered on database.<br>
HTTP method: GET<br>
Body as json: {"artist": "artist_name", "name": "music_name", "genre": "music_genre"}</p>
<br>

```'/home/register-music/genre-<genre>'```
<p>Route to register a music on database, choosing the genre of the music on "/genre-genre".<br>
HTTP method: POST<br>
Body as json: {"artist": "artist_name", "name": "music_name"}</p>
<br>

```/home/register-artist```
<p>Route to register an artist on database.<br>
HTTP method: POST<br>
Body as json: {"name": "artist_name", "genre": "artist_genre"}</p>
<br>

```/home/artists/<artist>```
<p>Route to delete an artist from database, passing artist name at the end of endpoint.<br>
HTTP method: DELETE<br></p>
<br>

```/home/musics/<music>```
<p>Route to delete a music from database, passing music name at the end of endpoint.<br>
HTTP method: DELETE<br></p>
<br>

```/home/edit/<music_or_artist>/<ID>```
<p>Route to edit the music or artist from database.<br>The user can choose between music or artist and him's ID in endpoint.</p>
<p>Example: </p>


```/home/edit/music/12```

<p>or</p>

```/home/edit/artist/4```
<p>HTTP method: PUT</p>
<br>

```/home/pop```
```/home/rap```
```/home/trap```
<p>Routes to return all musics registered as pop, rap or trap from database.<br>
HTTP method: GET<br>
Body as json: {"artist": "artist_name" ,"name": "music_name"}</p>
<br>