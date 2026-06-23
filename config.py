class Config:

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:root@localhost/vulnscanner"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "my_secret_key"