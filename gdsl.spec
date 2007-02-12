Summary:	Generic Data Structures Library
Summary(pl.UTF-8):   Biblioteka podstawowych struktur danych
Name:		gdsl
Version:	1.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.gna.org/gdsl/%{name}-%{version}.tar.gz
# Source0-md5:	9981f1ced783e30f50247e39179706bc
URL:		http://home.gna.org/gdsl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GDSL (Generic Data Structures Library) is a portable and
OS-independant generic data structures manipulation library fully
written in pure ANSI C from scratch, for C programmers. Most common
data structures are available with powerful algorithms and hidden
implementation. Available structures are lists, queues, stacks, hash
tables, binary trees, search binary trees, red-black trees, 2D arrays,
and permutations.

%description -l pl.UTF-8
GDSL (Generic Data Structures Library) to przenośna i niezależna od
systemu operacyjnego biblioteka operacji na podstawowych strukturach
danych, napisana od zera w czystym ANSI C, dla programistów C.
Większość ogólnych struktur danych jest dostępna wraz z potężnymi
algorytmami i ukrytą implementacją. Dostępne struktury to listy,
kolejki, stosy, tablice haszujące, drzewa binarne, drzewa wyszukiwań
binarnych, drzewa czerwono-czarne, tablice dwuwymiarowe i permutacje.

%package devel
Summary:	Header files and development documentation for Generic Data Structures Library
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do biblioteki podstawowych struktur danych
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for Generic Data Structures
Library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki podstawowych struktur
danych.

%package static
Summary:	Static Generic Data Structures Library
Summary(pl.UTF-8):   Statyczna biblioteka podstawowych struktur danych
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Generic Data Structures Library.

%description static -l pl.UTF-8
Statyczna biblioteka podstawowych struktur danych.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc src/examples/* doc/html/*.html doc/html/*.css doc/html/*.png
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/gdsl
%{_includedir}/gdsl/*.h
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
