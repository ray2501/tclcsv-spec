#!/usr/bin/tclsh

set arch "x86_64"
set base "tclcsv-2.3"
set fileurl "https://sourceforge.net/projects/tclcsv/files/tclcsv-2.3-src.tar.gz"

set var [list wget $fileurl -O $base-src.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base-src.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tclcsv.spec]
exec >@stdout 2>@stderr {*}$buildit

file delete $base-src.tar.gz

