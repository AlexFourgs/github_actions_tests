#!/usr/bin/env python3

"""Main file for dipy-version

This module provides __version__ attribute and function called when dipy-version
is invoked.
"""

import argparse
import sys
from distutils import version

__version__ = '6.33.0'


def dipy(args):
    """Function called when the script dipy-version is used.

    Parameters
    ----------
    args: list
        The arguments passed to dipy-version.
    """
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    # add parameters
    arg_parser.add_argument('--is-higher', help='Version to compare.',
                            type=str, required=False)

    args = arg_parser.parse_args(args)

    min_version_required = args.is_higher

    # compare version
    if min_version_required:
        if version.StrictVersion(min_version_required) > version.StrictVersion(
                __version__):
            sys.exit('Dipy version installed ({}) does not fit with the minimum'
                     ' version required ({}).'.format(__version__,
                                                      min_version_required))
    else:
        print(__version__)



def dipy_version_github_action():
	"""Print Dipy version with format for Github Actions

	See https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
	for more details.
	"""
	print(f'::set-output name=dipy_version::{__version__}')


# used by Github actions
if __name__ == '__main__':
    dipy_version_github_action()
