#!/bir/bash
pkg install subversion -y
pkg install python -y
pkg install libjpeg-turbo libcrypt ndk-sysroot clang zlib -y
pkg install libjpeg-turbo -y
LDFLAGS=" -lm" pip3 install pillow
pkg install nano -y
pkg install vim -y
pip3 install -r requirements.txt
