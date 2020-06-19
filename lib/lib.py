"""Library for the FolderMaker project"""
from os import chdir, mkdir

def conf_to_starr(path):
    """Read the config from `path` and return it as a list of strings"""
    with open(path, 'r') as conf_file:
        return [x.strip() for x in conf_file.readlines()]


def split_types(indata):
    """Split the list of strings into list of tuples (dat, type)"""
    dat_list = []
    for conf_line in indata:
        starr = conf_line.split('?')
        dat_list.append((starr[0], starr[1]))
    return dat_list

def create_dirs(tup_arr_dat, basedir, range_x):
    """Create directories"""
    chdir(basedir)
    for i in range_x:
        mkdir(str(i))
        chdir(str(i))
        for (dir_name, _) in tup_arr_dat:
            mkdir(dir_name)
        chdir('..')
