import zipfile
import os
from glob import glob
from ruamel.std.zipfile import delete_from_zip_file  # pip install ruamel.std.zipfile

# ZipLib by SiniKraft !
# requires lzma module to be included


def close_zip(newzip):
    """Close an open zipfile
    Usage : close_zip(z)"""
    newzip.close()


def read_zip(zip_file):
    """Open a zip from location to use as zipfile object with other functions.
    You'll need to close the zipfile with close_zip() if the functions used does not do it.
    Usage : z = read_zip('my_file.zip')"""
    return zipfile.ZipFile(zip_file, 'r', zipfile.ZIP_LZMA)


def write_zip(zip_file):
    """Open a zip in write mode, to use it with functions.
    You''l also need to close it.
    Usage : z = write_zip('my_file.zip')"""
    return zipfile.ZipFile(zip_file, 'a', zipfile.ZIP_LZMA)


def add_to_zip(file, newzip, archive_location="", close=True):
    """Add a file to the archive.
    The archive location parameter allows you to specify where the file should be located in the archive and its name.
    It supports subdirectories in the archive.
    WARNING: You can add same file names in the archive but it's not recommended.
    You need to have a zipfile object opened with write_zip().
    Usage : add_to_zip('to_add.txt', z)
    The close parameter specify if the zipfile object should be closed after doing the operation."""
    if archive_location == "":
        archive_location = os.path.basename(file)
    newzip.write(file, arcname=archive_location)
    if close:
        newzip.close()


def read_file(file, newzip, close=True):
    """Read a file in the archive and return its raw data
    You need to have a zipfile object opened with read_zip().
    Usage : read_file('file.txt', z)
    The close parameter specify if the zipfile object should be closed after doing the operation."""
    data = newzip.read(file)
    if close:
        newzip.close()
    return data


def extract_file(file, newzip, new_dir, close=True):
    """Extract a file from the archive to another location.
    The source file stays in the archive.
    Usage : extract_file('file.txt', z, os.path.expandvars('%USERPROFILE%\\Downloads\\'))
    You need to have a zipfile object opened with read_zip()."""
    newzip.extract(file, new_dir)
    if close:
        newzip.close()


def extract_all(newzip, new_dir, close=True):
    """Extract all files from the archive to another location.
    The source files stay in the archive.
    Usage : extract_all(z, os.path.expandvars('%USERPROFILE%\\Downloads\\'))
    You need to have a zipfile object opened with read_zip()."""
    newzip.extractall(new_dir)
    if close:
        newzip.close()


def list_all_elements(newzip, close=True):
    """Return a list of all elements which are in the archive.
    Usage : list_all_elements(z)
    You need to have a zipfile object opened with read_zip()."""
    data = newzip.namelist()
    if close:
        newzip.close()
    return data


def add_all_files_to_zip(folder, newzip, close=True):
    """Will add in the archive all files from a folder.
    Subdirectories files will not be added.
    The source files are not deleted.
    You need to have a zipfile object opened with write_zip().
    Usage : add_all_files_to_zip(os.path.expandvars('%USERPROFILE%\\Downloads\\'), z)"""
    files = glob(folder + "*.*")
    for file in files:
        newzip.write(file, arcname=os.path.basename(file))
    if close:
        newzip.close()


def delete_zip(newzip):
    """Simply delete a zip file.
    Usage : delete_zip('my_file.zip')"""
    os.remove(newzip)


def delete_file_from_zip(newzip, file):
    """Delete a file in a archive.
    You need to have a zipfile object opened with write_zip().
    Usage : delete_file_from_zip(z, 'file.txt')"""
    delete_from_zip_file(newzip, file_names=[str(file)])
