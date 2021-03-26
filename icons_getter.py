# ICONS GETTER MODULE BY SINIKRAFT #
# Check out : 'github.com/SiniKraft' ! #

# Icons Getter can be used to generate a .png file with the icon of a specified file, including previews. #
# Icons Getter is a java package, and this library add python compatibility #

# Needs a java jdk to be in the same folder, in "jdk" folder#

import subprocess


def get_icon(source, target, is_large=True, show_window=False):
    """
    :param show_window: Specify if a window with the icon on it should appears. Default: False
    :param is_large: If True, generate a 32 * 32 icon instead of a basic 16 * 16 one. Default: True
    :param target: Specify where to save the icon and the json metadata files.
    :param source: Specify which file should be previewed.
    """
    args = "{0} {1} {2} {3}".format(str(source), str(target), bool(is_large), bool(show_window))

    try:

        print("icons getter output : {0}".format(subprocess.check_output('"jdk\\java-se-8u41-ri\\bin\\java.exe" -jar '
                                                                         'icons_getter.jar {0}'.format(args),
                                                                         shell=True, stderr=subprocess.STDOUT)))
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
