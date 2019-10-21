from env import user, host, password

def get_db_url(db):
        return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# Grabs the database using env file.