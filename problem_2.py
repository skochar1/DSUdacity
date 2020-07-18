###############################################################################
# 1st way (using global list and just appending to it as we see suffix files) #
###############################################################################
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []
    file_finder(suffix, path, result)
	return result
    
def file_finder(suffix, path, result)
    "...\Desktop\tesdir\subdir1"
    # os.listdir(path) == ['subdir1', 'subdir2', 'subdir3', 'subdir4', 'subdir5', 't.c', 't.h']
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
            
        if os.path.isdir(child_path):
            file_finder(suffix, child_path, result)
          
        elif os.path.isfile(child_path) and child.endswith(suffix):
            result.append(child_path)  

            
#############################################
# 2nd way of doing it (using result.extend) #
#############################################
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []
    "...\Desktop\tesdir\subdir1"
    # os.listdir(path) == ['subdir1', 'subdir2', 'subdir3', 'subdir4', 'subdir5', 't.c', 't.h']
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
            
        if os.path.isdir(child_path):
            result.extend(file_finder(suffix, child_path))
          
        elif os.path.isfile(child_path) and child.endswith(suffix):
            result.append(child_path)
    
    return result

                  
    def main():
        path = r"/Users/shreyakochar/Desktop/testdir"
        file_finder(".c", path)

                  
    if __name__ == "__main__":
        main()


## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python
import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))