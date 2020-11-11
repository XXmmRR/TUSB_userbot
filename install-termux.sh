#!/bir/bash
pkg upgrade -y
pkg update -y
pkg install python -y
pkg install libjpeg-turbo libcrypt ndk-sysroot clang zlib -y
pkg install libjpeg-turbo -y
LDFLAGS=" -lm" pip3 install pillow
pkg install nano
pkg install vim-python
cd TUSB_userbot
cd TUSB
pip3 install -r requerements.txt
