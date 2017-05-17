# libapicache
Python 3 interface library for [APICache](https://github.com/SOBotics/apicache)

## Installation
Use Python 3 `pip` (either with `--user` for a per-user install, or with `sudo` for a global install):

    $ pip3 install libapicache --user
    # OR #
    $ sudo -H pip3 install libapicache
    
## Usage

```python
from libapicache import APICache


cache = APICache('https://cache.example.org')  # no trailing slash
response = cache.posts_by_id(['38472654'], key='IQlbo34sc932sdrg23((', site='stackoverflow.com')

if not response.is_error():
    for post in response.items:
        print("Got post {} from Stack Overflow. Score: {}".format(post['post_id'], post['score']))
else:
    print("Uh oh! Error: {} (ID: {})".format(response.error_message, response.error_id))
```

Refer to APICache's documentation (visit `/docs/quickstart` on your chosen APICache server) for further information
about the routes libapicache is calling.
