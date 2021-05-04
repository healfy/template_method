import os
import app


class Settings:
    BASE_DIR: str = os.path.dirname(os.path.abspath(app.__file__))
