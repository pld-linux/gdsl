Summary:	Generic Data Structures Library
Summary(pl):	Biblioteka podstawowych struktur danych
Name:		gdsl
Version:	1.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://freesoftware.fsf.org/download/gdsl/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
URL:		http://www.freesoftware.fsf.org/gdsl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GDSL (Generic Data Structures Library) is a portable and
OS-independant generic data structures manipulation library fully
written in pure ANSI C from scratch, for C programmers. Most common
data structures are available with powerful algorithms and hidden
implementation. Available structures are lists, queues, stacks, hash
tables, binary trees, search binary trees, red-black trees, 2D arrays,
and permutations.

%package devel
Summary:	Header files and development documentation for Generic Data Structures Library
Summary(pl):	Pliki nagłówkowe i dokumentacja do biblioteki podstawowych struktur danych
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for Generic Data Structures
Library.

%description devel -l pl
Pliki nagłówkowe i dokumentacja do biblioteki podstawowych struktur
danych.

%package static
Summary:	Static Generic Data Structures Library
Summary(pl):	Statyczna biblioteka podstawowych struktur danych
Group:		Development/Libraries

%description static
Static Generic Data Structures Library.

%description static -l pl
Statyczna biblioteka podstawowych struktur danych.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc src/examples/* README TODO
%attr(755,root,root) %{_libdir}/*.so.?
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/gdsl/*.h

%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
