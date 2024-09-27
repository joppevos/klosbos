# install packages

```
python -m venv venv
source venv/bin/activate
pip install "fastapi[standard]" requests
```

# start server

`fastapi dev server.py`

# run client request

```python
python
client.py

`Response
from FastAPI: {'answer': "Sorry, I couldn't process your question at the moment."}
```

# docker
`docker build -t myimage .`


`docker run -d --name mycontainer -p 80:80 myimage`


docs:
`http://127.0.0.1/docs`
