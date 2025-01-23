def login(user_type):
    print(f"Logging in as {user_type}...")
    if user_type == "administrator":
        print("Administrator access granted.")
        return True
    elif user_type == "normal_user":
        print("Normal user access granted.")
        return True
    else:
        print("Access Denied. Invalid user  type.")
        return False
    

def crud_permission(user_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Checking permission for {func.__name__}...")
            if login(user_type):
                print(f"Permission granted for {user_type}. Executing {func.__name__}...")
                return func(*args, **kwargs)
            else:
                print("permission denied . Cannot execute the function.")
                return None
        return wrapper
    return decorator





@crud_permission("administrator")
def create(data):
    print(f"Creating data: {data}")
    return f"Data {data} created!"


@crud_permission("normal_user")
def read():
    print("Reading data...")
    return "Data read successfully!"


@crud_permission("administrator")
def update(data_id, new_data):
    print(f"Updating data ID {data_id} to {new_data}")
    return f"Data ID {data_id} updated to {new_data}."




@crud_permission("normal_user")
def delete(data_id):
    print(f"Deleting data ID {data_id}")
    return f"Data ID {data_id} deleted!"





print(create("Sample Data"))
print(read())
print(update(1,"Updated Data"))
print(delete(1))