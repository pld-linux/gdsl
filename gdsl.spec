Summary:	Generic Data Structures Library
Summary(pl):	Biblioteka podstawowych struktur danych
Name:		gdsl
Version:	1.0
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://freesoftware.fsf.org/download/gdsl/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
URL:		http://www.freesoftware.fsf.org/gdsl/
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

%description -l pl
GSSL (Generic Data Structues Library) to przeno¶na i niezale¿na od
systemu operacyjnego biblioteka operacji na podstawowych strukturach
danych, napisana od zera w czystym ANSI C, dla programistów C.
Wiêkszo¶æ ogólnych struktur danych jest dostêpna wraz z potê¿nymi
algorytmami i ukryt± implementacj±. Dostêpne struktury to listy,
kolejki, stosy, tablice haszuj±ce, drzewa binarne, drzewa wyszukiwañ
binarnych, drzewa czerwono-czarne, tablice dwuwymiarowe i permutacje.

%package devel
Summary:	Header files and development documentation for Generic Data Structures Library
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki podstawowych struktur danych
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for Generic Data Structures
Library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki podstawowych struktur
danych.

%package static
Summary:	Static Generic Data Structures Library
Summary(pl):	Statyczna biblioteka podstawowych struktur danych
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Generic Data Structures Library.

%description static -l pl
Statyczna biblioteka podstawowych struktur danych.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc src/examples/* README TODO
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%dir %{_includedir}/gdsl
%{_includedir}/gdsl/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
