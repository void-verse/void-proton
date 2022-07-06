import sys
import os
from proton.utils import msg, err
from proton.core.errors import ManagerArgumentError
from proton import Proton


def runner(app: Proton):
    main_file = sys.argv[0].replace(".py", "")
    command = sys.argv[1].split(":")[0]
    param = sys.argv[1].split(":")[1]
    if command == "run":
        if param == "db":
            print(msg("RUN", "Database"))
            app.database.boot()
            print("\n", msg("END", "Database"))
        else:
            print(msg("RUN", "Server"))
            os.system(f"gunicorn {main_file}:{param} {app.gunicorn_config()}")
            print(msg("END", "Server"))
    elif command == "create":
        if param == "admin":
            pass
        else:
            pass
    elif "gunicorn" in sys.argv[0]:
        print(
            msg(
                "MSG",
                f"Running server at *http://{app.host}:{app.port}*\n\t\bUse *CTRL+C* to stop the server",
            )
        )
