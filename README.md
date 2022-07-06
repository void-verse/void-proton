# PROTON : A proton sized web framework

Proton is an Express inspired proton sized web framework for building backend web applications from [void](https://github.com/void-verse). Currently, it has features of adding routes, controllers and sending API responses (Refer the [example blog app](https://github.com/NandanunniAS/Nano-Blog-App) for reference). Defining models with custom field types is also available but is under development.

**Status** : Under developement
<br />

### To run example app

```bash
$ pip3 install -r requirements.txt

$ python3 main.py run:<appname>
```

## Documentation

**Step 1**: Install proton and create folder structure

```bash
$ pip3 install proton-py

$ touch models.py
$ touch controllers.py
$ touch routes.py
$ touch main.py
```

<br />

**Step 2**: Define your models

```python
# models.py
from proton.db import model

class User(model.Model):
    username = model.StringType('username', max_length=50, min_length=4, unique=True, required=True)
    # define your model here
```

<br />

**Step 2**: Define your controllers

```python
# controllers.py
from proton.handler import Response

def index(req):
    # define your controller here
    return Response(status=200, data={"msg": "message"})
```

<br />

**Step 3**: create a router and assign controllers with routes

```python
# routes.py
from proton.handler import Router
from .controllers import index

router = Router()
router.get("/", index)
```

<br />

**Step 4**: create proton app and assemble your router and models

```python
# main.py
from proton import Proton, run
from .routes import router
from .models import User

api = Proton()

api.set_router('/api', router)
api.set_models(User)

run(api)
```

<br />

**Step 5**: Boot your models to db and run the server

```bash
$ python3 main.py run:db
$ python3 main.py run:api
```

Refer the [example blog app](https://github.com/NandanunniAS/Nano-Blog-App) for folder structure. Working on a better documentation
