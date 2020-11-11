#!/bir/bash
pkg install python -y
pkg install libjpeg-turbo libcrypt ndk-sysroot clang zlib -y
pkg install libjpeg-turbo -y
LDFLAGS=" -lm" pip3 install pillow
pkg install nano
pkg install vim-python
