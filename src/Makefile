libj-full:
	@make libj32
	@make libj64

libj32:
	@gcc -ffreestanding -nostdlib -shared -melf_i386 -Ilibj/include -o example/resources/native/libj32.so libj/src/main.c

libj64:
	@gcc -ffreestanding -nostdlib -shared -Ilibj/include -o example/resources/native/libj64.so libj/src/main.c

install:
	sudo cp -rf jetpy /usr/jetpy
	sudo ln -s /usr/jetpy/jetpy.py /usr/bin/jetpy

uninstall:
	sudo rm -rf /usr/jetpy
	sudo rm /usr/bin/jetpy

update:
	make uninstall
	make install
