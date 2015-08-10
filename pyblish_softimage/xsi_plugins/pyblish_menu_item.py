"""Add Pyblish to file-menu"""

def XSILoadPlugin(in_reg):
	from win32com.client import constants

	in_reg.Name = "Pyblish_Qt"
	in_reg.Author = "Marcus Ottosson"
	in_reg.Email = "marcus@abstractfactory.io"
	in_reg.Major = 1
	in_reg.Minor = 0
	in_reg.RegisterCommand("Pyblish_Qt")
	# http://docs.autodesk.com/SI/2015/ENU/Softimage-Developer-Help//index.html#!/url=./si_cpp/namespaceXSI.html#af9700f1d68da1287ef23c3f26687bc2aaff76fe6f8fb802accec08c55124e4a4e
	in_reg.RegisterMenu(constants.siMenuMainFileSceneID,
						"Pyblish_Qt_Menu", False, False)

def Pyblish_Qt_Menu_Init(in_ctxt):
	oMenu = in_ctxt.Source
	oMenu.AddCommandItem("Pyblish", "Pyblish_Qt")

	return True

def Pyblish_Qt_Execute():
	show()
