default: gui.py foldersDialog.py
	echo "built"
	
gui.py: GUI/gui.ui
	pyuic5 GUI/gui.ui -o gui.py
	
foldersDialog.py: GUI/foldersDialog.ui
	pyuic5 GUI/foldersDialog.ui -o foldersDialog.py
clean: 
	rm -f *.json
	rm -f gui.py
	rm -f foldersDialog.py
	rm -rf __pycache__
