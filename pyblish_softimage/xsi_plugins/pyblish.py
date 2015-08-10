"""Pyblish for Softimage start-up plug-in

Usage:
    Add the directory of this file to your
    environment as XSI_PLUGIN.

"""


import win32com.client
from win32com.client import constants

null = None
false = 0
true = 1


def XSILoadPlugin(in_reg):
    in_reg.Author = "marcus"
    in_reg.Name = "NewEvent Plug-in"
    in_reg.Major = 1
    in_reg.Minor = 0

    #RegistrationInsertionPoint - do not remove this line

    import pyblish_softimage
    pyblish_softimage.setup()

    return true


def XSIUnloadPlugin(in_reg):
    strPluginName = in_reg.Name

    Application.LogMessage(
        str(strPluginName) + str(" has been unloaded."),
        constants.siVerbose)

    return true
