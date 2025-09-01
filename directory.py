# # creat a python directoryory if it does not exist
# import os
# def create_directory(path):
#     if not os.path.exists(path):
#         os.makedirs(path)
#         print(f"Directory {path} created.")
#     else:
#         print(f"Directory {path} already exists.")  
# # Example usage
# create_directory("example_directory")      

# os.chdir("example_directory")
# print("Current Working Directory:", os.getcwd())

# # create a sub directory
# sub_dir = "sub_directory"
# if not os.path.exists(sub_dir):
#     os.makedirs(sub_dir)
#     print(f"Sub-directory {sub_dir} created.")
# else:
#     print(f"Sub-directory {sub_dir} already exists.")

# # change to sub directory
# os.chdir(sub_dir)
# print("Current Working Directory:", os.getcwd())

# # to list the contents 
# print("Contents of the current directory:", os.listdir())


import os

# Step 1: Create a directory (only if it doesn't exist)
# if not os.path.exists("Old_Dir"):
#     os.mkdir("Old_Dir")
#     print("Directory 'Old_Dir' created.")

# Step 2: Rename directory
# os.rename("Old_Dir", "New_Dir")
# print("Directory renamed from 'Old_Dir' to 'New_Dir'.")

# Step 3: Show current contents
# print("Current directories/files:", os.listdir())

# # use rmdir
# os.rmdir("New_Dir")
# print("Directory 'New_Dir' removed.")


# Create directory if it doesn't exist
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")

# Check if it's a directory
if os.path.isdir("MyFolder"):
    print("'MyFolder' is a directory.")
else:
    print("'MyFolder' is NOT a directory.")
