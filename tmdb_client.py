import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OWQ1ZGM2MDBiYjgxMWYwYmE5MTNiYTc2MGZiZDhmYSIsInN1YiI6IjVmNWE4MTBiMGU0NDE5MDAzNWY4YWRiMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RhFHs3TofYE56PE1aL0q56SGIB72WpUMzSxRLb_lyzs"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"    

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OWQ1ZGM2MDBiYjgxMWYwYmE5MTNiYTc2MGZiZDhmYSIsInN1YiI6IjVmNWE4MTBiMGU0NDE5MDAzNWY4YWRiMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RhFHs3TofYE56PE1aL0q56SGIB72WpUMzSxRLb_lyzs"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

