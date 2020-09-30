build: gui.py
	echo "build test"

gui.py: src/GUI/gui.ui
	make -C src/makefile
	cp main.py build/main.py
	cp steam.py build/steam.py
clean:
	rm -rf build
