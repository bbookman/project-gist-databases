from .models import Gist
import pdb

def search_gists(db_connection, **kwargs):
    results = []
    
    query = 'SELECT * from gists'
    if not kwargs:
        query = query
    elif kwargs == 'github_id':
        query += 'WHERE github_id = :github_id'
    elif kwargs == 'created_at':
        query += 'WHERE created_at = :created_at'
    data = db_connection.execute(query)
    for gist in data:
        results.append(Gist(gist))
        #pdb.set_trace()
        print(str(Gist(gist)))
    return results
    