import psycopg2

def main():
    # Connection string
    conn_str = 'postgresql://postgres:geN4f1tSdhMePbgd@fretfully-refreshing-iguanodon.data-1.use1.tembo.io:5432/postgres'

    try:
        # Create a new database session
        conn = psycopg2.connect(conn_str)
    except Exception as e:
        print(f"Unable to connect to the database: {e}")

    try:
        # Create a new cursor object.
        cur = conn.cursor()

        # Test Query
        cur.execute("SELECT 1")

        # Fetch result
        output = cur.fetchone()[0]
        print(output)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close communication with the database
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()