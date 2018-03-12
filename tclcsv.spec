#
# spec file for package tclcsv
#

Name:           tclcsv
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  tcl-devel >= 8.6
Requires:       tcl >= 8.6
Summary:        Reading and writing CSV format files for Tcl
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Version:        2.3
Release:        0
Url:            https://tclcsv.magicsplat.com/
Source0:        %{name}-%{version}-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tclcsv is a extension for reading and writing CSV format files.
It also includes a Tk widget for configuring CSV formats.

%prep
%setup -q -n %name-%version-src

%build
chmod 755 configure
./configure \
	--libdir=%_libdir \
	--prefix=/usr \
	--with-tcl=%_libdir

%install
make install \
	DESTDIR=%buildroot \
        pkglibdir=%{tcl_archdir}/%{name}%{version}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{tcl_archdir}/%{name}%{version}

%changelog
