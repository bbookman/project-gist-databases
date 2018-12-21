from .models import Gist
import pdb

def search_gists(db_connection, **kwargs):
    results = []
    
    query = 'SELECT * from gists '
    if not kwargs:
        query = query
        data = db_connection.execute(query)
    else:
        if 'github_id' in kwargs:
            query += 'WHERE github_id = :github_id'
        elif 'created_at' in kwargs:
            query += 'WHERE datetime(created_at) = datetime(:created_at)'

        data = db_connection.execute(query, kwargs)
        
    for gist in data:
        results.append(Gist(gist))
        #pdb.set_trace()
        print(str(Gist(gist)))
    return results
    
    
    
    '''
    params = {
  'created_at': datetime(2014, 5, 3, 20, 26, 8)
}
cursor = db.execute("""
  SELECT *
  FROM
    gists
  WHERE
    datetime(created_at) == datetime(:created_at)
""", params)
    
    '''