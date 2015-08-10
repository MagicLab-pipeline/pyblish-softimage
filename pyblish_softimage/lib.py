# Standard library
import os
import contextlib

# Pyblish libraries
import pyblish.api
import pyblish_integration

# Local libraries
import plugins
Application = globals()["Application"]

show = pyblish_integration.show


def setup(console=False):
    """Setup integration

    Registers Pyblish for Maya plug-ins and appends an item to the File-menu

    Attributes:
        preload (bool): Preload the current GUI
        console (bool): Display console with GUI

    """

    pyblish_integration.setup(console)

    register_plugins()
    add_to_filemenu()
    register_host()

    pyblish_integration.echo("pyblish: Integration loaded..")


def register_host():
    """Register supported hosts"""
    pyblish.api.register_host("xsi")
    pyblish.api.register_host("softimage")


def register_plugins():
    # Register accompanying plugins
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.register_plugin_path(plugin_path)
    pyblish_integration.echo("pyblish: Registered %s" % plugin_path)


def add_to_filemenu():
    """Add Pyblish to file-menu"""

    def XSILoadPlugin(in_reg):
        from win32com.client import constants

        in_reg.Name = "Pyblish_Qt"
        in_reg.Author = "Marcus Ottosson"
        in_reg.Email = "marcus@abstractfactory.io"
        in_reg.Major = 1
        in_reg.Minor = 0
        in_reg.RegisterCommand("Pyblish_Qt")
        in_reg.RegisterMenu(constants.siMenuMainFileImportID,
                            "Pyblish_Qt_Menu", False, False)

    def Pyblish_Qt_Menu_Init(in_ctxt):
        oMenu = in_ctxt.Source
        oMenu.AddCommandItem("Pyblish", "Pyblish_Qt")

        return True

    def Pyblish_Qt_Execute():
        show()


@contextlib.contextmanager
def maintained_selection():
    """Maintain selection during context

    Example:
        >>> with maintained_selection():
        ...     # Modify selection
        ...     app.Select("node', replace=True)
        >>> # Selection restored

    """

    pass
