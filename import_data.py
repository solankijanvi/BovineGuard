import pandas as pd
from sqlalchemy import create_engine

def import_csv_to_db(csv_file):
    # Load CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Create a database engine
    engine = create_engine('sqlite:///cattle_diseases.db')

    # Write DataFrame to SQL table
    df.to_sql('cattle_diseases', engine, if_exists='replace', index=False)

if __name__ == '__main__':
    import_csv_to_db('cattle_disease_data.csv')
