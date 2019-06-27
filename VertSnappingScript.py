import maya.cmds as cmds

def start(direction):
	currentSelections = cmds.ls(sl=True,fl=1)
	broken = breaker(currentSelections)

	if (broken == False):
		best = findHeight(currentSelections,direction[0],direction[1])
		moveHeight(currentSelections,direction[0],direction[1],best)
		confirmMessage()

def breaker(currentSelections):
	broken = False
	if currentSelections >= 1 :
		selectedVerts = cmds.polyEvaluate( vertexComponent=True )
		if len(currentSelections) != selectedVerts:
			cmds.warning("please select only verts; aborted")
			broken =True

	if len(currentSelections) < 2 :
		cmds.warning("please select at least 2 verts; aborted")
		broken =True
	return broken

def findHeight(currentSelections,posNeg,axis):
	currentBest = None
	
	for verts in currentSelections:
		vertPosition = cmds.pointPosition(str(verts),w=True)

		if (axis == "X"):
			xpos = vertPosition[0]
			if (posNeg == "-"):
				if (xpos < currentBest or currentBest == None):
					currentBest = xpos
			if (posNeg == "+"):
				if (xpos > currentBest or currentBest == None):
					currentBest = xpos
		if (axis == "Y"):
			ypos = vertPosition[1]
			if (posNeg == "-"):
				if (ypos < currentBest or currentBest == None):
					currentBest = ypos
			if (posNeg == "+"):
				if (ypos> currentBest or currentBest == None):
					currentBest = ypos
		if (axis == "Z"):
			zpos = vertPosition[2]
			if (posNeg == "-"):
				if (zpos < currentBest or currentBest == None):
					currentBest = zpos
			if (posNeg == "+"):
				if (zpos > currentBest or currentBest == None):
					currentBest = zpos
	return currentBest

def moveHeight(currentSelections,posNeg,axis,best):
	for verts in currentSelections:
		vertPosition = cmds.pointPosition(str(verts),w=True)
		
		if (axis == "X"):
			cmds.move(best,x=True,yz=False,a=True)

		if (axis == "Y"):
			cmds.move(best,y=True,xz=False,a=True)

		if (axis == "Z"):
			cmds.move(best,z=True,xy=False,a=True)
	
def createUI():
	windowWidth = 140
	if cmds.window("MainWindow_VertSnappingTool", exists=True):
		cmds.deleteUI ("MainWindow_VertSnappingTool", window=True)
	    
	if cmds.windowPref( "MainWindow_VertSnappingTool", exists=True ):
		cmds.windowPref( 'MainWindow_VertSnappingTool', remove=True )
  
	cmds.window("MainWindow_VertSnappingTool", title=" ", minimizeButton=False, maximizeButton=False, sizeable=False)
	cmds.columnLayout("mainUI_C", parent="MainWindow_VertSnappingTool")

	cmds.rowColumnLayout(numberOfColumns=3, cw=[(1, windowWidth * .33),(2,windowWidth * .33),(3,windowWidth* .33)], p="mainUI_C")
	
	cmds.button(l="-X",h=windowWidth * .33, bgc =(.8,.2,.2), c=lambda arg: start(["-","X"]))
	cmds.button(l="+Y",h=windowWidth * .33, bgc =(.2,.8,.2), c=lambda arg: start(["+","Y"]))
	cmds.button(l="+X",h=windowWidth * .33, bgc =(.8,.2,.2), c=lambda arg: start(["+","X"]))
	cmds.button(l="-Z",h=windowWidth * .33, bgc =(.2,.2,.8), c=lambda arg: start(["-","Z"]))
	cmds.button(l="-Y",h=windowWidth * .33, bgc =(.2,.8,.2), c=lambda arg: start(["-","Y"]))
	cmds.button(l="+Z",h=windowWidth * .33, bgc =(.2,.2,.8), c=lambda arg: start(["+","Z"]))
	
	cmds.showWindow("MainWindow_VertSnappingTool")      
def header():
	print "-"* 50
	print "#"*50
	print "-"* 50
	print ""
	print " DumpsterTree Tools"
	print " DumpsterTree.com"
	print " DumpsterTree@gmail.com"
	print ""
	print " Thanks you for choosing Dumpstech Artistree"
	print "	-Zachary Collins"
	print ""
	print "-"* 50
	print "#"*50
	print "-"* 50
def footer():
	print "-"* 50
	print "#"*50
	print "-"* 50
	print ""
	print "Thank you!"
	print "comments, questions and concerns can be sent to,"
	print "DumpsterTree@gmail.com"
	print ""
	print "-"* 50
	print "#"*50
	print "-"* 50
def confirmMessage():
	print""
	print ("successfully executed;")

createUI()
header()

cmds.scriptJob( uid = ["MainWindow_VertSnappingTool",footer], protected=True)