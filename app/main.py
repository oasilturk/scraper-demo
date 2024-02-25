import db

def main():
    try:
        result = db.insert_test_data()
        print(f"Inserted data with ID: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
