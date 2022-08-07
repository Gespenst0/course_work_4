from app.config import BaseConfig
from app.server import create_app

app = create_app(BaseConfig)
app.config.from_envvar("APP_SETTINGS", silent=True)

if __name__ == '__main__':
    app.run()