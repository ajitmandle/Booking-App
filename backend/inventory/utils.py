import psycopg2
from django.conf import settings
import pandas as pd
from io import StringIO

def load_csv_to_db(file_path, table_name, separator=','):
    """Load CSV data into a PostgreSQL table using COPY command."""
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()
        df = pd.read_csv(file_path)
        df = df.applymap(lambda x: x.replace("\n", " ") if isinstance(x, str) else x)
        print(df)
        columns=df.columns.to_list()
        # Convert DataFrame to CSV format in memory (without index column)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False, header=False,sep='#')  # No header for `copy_from`
        csv_buffer.seek(0)
        cursor.copy_from(csv_buffer,table_name,sep='#',columns=columns)

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Data successfully loaded into {table_name}")

    except Exception as e:
        print(f"Error loading CSV into {table_name}: {e}")
