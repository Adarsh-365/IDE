import os

# direc = {}
# def list_files_and_folders(directory,direc=direc):
   
#         # Get all items (files and folders) in the directory
#     items = os.listdir(directory)
    
#     print(directory)
#     for item in items:
#         print(item)
#         item_path = os.path.join(directory, item)
#         if os.path.isdir(item_path):
           
#             list_files_and_folders(directory+"/"+item,direc)
#             direc["Folder"] = f"📁 {item} (Folder)"
            
#         else:
#                 direc["Folder"] = f"📄 {item} (File)"
#     return direc   
  
import os

def list_files_and_folders(directory):
    directory_structure = {}

    # Get all items (files and folders) in the directory
    items = os.listdir(directory)
    Files = []
    folder = []
    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            # Add folder as a dictionary and recurse
            directory_structure[item] = list_files_and_folders(item_path)
            folder.append(item)
            
           
        else:
            # Add file as a string
            Files.append(item)
    directory_structure['Folder'] =folder
    directory_structure['Files'] = Files
    
    return directory_structure


