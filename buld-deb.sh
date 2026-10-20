#!/bin/sh
set -e
VERSION="${1:-1.0.0}"
PKG="carnival_${VERSION}_all"
MAIN="main.py"

rm -rf "$PKG"
mkdir -p "$PKG/DEBIAN" "$PKG/usr/bin" "$PKG/usr/share/carnival"

tar --exclude=./.git --exclude=./.github --exclude=./build-deb.sh \
    --exclude='./carnival_*' --exclude='__pycache__' \
    -cf - . | tar -xf - -C "$PKG/usr/share/carnival"

cat > "$PKG/usr/bin/carnival" <<EOF
#!/bin/sh
exec python3 /usr/share/carnival/$MAIN "\$@"
EOF
chmod 755 "$PKG/usr/bin/carnival"

cat > "$PKG/DEBIAN/control" <<EOF
Package: carnival
Version: $VERSION
Architecture: all
Maintainer: Odin Kirkham okir9913@gmail.com
Depends: python3
Description: A cabinet of terminal games
 A collection of small command-line games written in Python.
EOF

dpkg-deb --build --root-owner-group "$PKG"
echo "Built $PKG.deb"