build: gui.py
	echo "build test"
gui.py: GUI/gui.ui
	mkdir -p build
	pyuic5 GUI/gui.ui -x -o build/gui.py
clean:
	rm -rf build
