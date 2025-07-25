import os
import os.path


'''
kinds of sheets

kind #1:
- sheet has one background color
- sprites have a SINGLE bounding rect, one different color from bg

kind #2:
- sheet has one background color
- sprites have ONE OR MORE bounding rect, one different color from bg

kind #3:
- sheet has one background color
- sprites have ONE OR MORE bounding rect, many different colors from bg
'''

# returns a list of absolute path names to every file in the folder specified
# NOTE: files are searched for recursively
def get_files(root_path):
    assert(os.path.isdir(root_path) == True)
    filepaths = []
    for path in os.listdir(root_path):
        temp_path = os.path.join(root_path, path)
        if os.path.isdir(temp_path):
            filepaths = filepaths + get_files(temp_path)
        elif os.path.isfile(temp_path):
            filepaths.append(temp_path)
    return filepaths
