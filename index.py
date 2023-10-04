import os
import pandas as pd

def classify_items(directory_path):
  items = []
  for root, directories, files in os.walk(directory_path):
    for directory in directories:
      folder_path = os.path.join(root, directory)
      num_children = len(os.listdir(folder_path))
      items.append(("Folder", folder_path, num_children, None))
      
    for file in files:
      file_path = os.path.join(root, file)
      file_size = os.path.getsize(file_path)
      items.append(("File", file_path, None, file_size))
      
  return items
   
   
   
directory_path = 'C:/Users/placeholder/placeholder/'
items = classify_items(directory_path)
df = pd.DataFrame(items, columns = ['Type', 'Path', 'Number of Children', 'Size'])
df['Hierarchy'] = df['Path'].apply(lambda x:x[len(directory_path):].count(os.path.sep))
df = df.sort_values(by = ['Hierarchy', 'Path']).reset_index(drop=True)

print(df)
