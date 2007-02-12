Summary:	Janus library
Summary(pl.UTF-8):   Biblioteka Janus
Name:		janus
Version:	0.4.4.20020912
Release:	1
License:	LGPL
Group:		Libraries
#Source0:	ftp://victor.worldforge.org/pub/worldforge/libs/janus/%{name}-%{version}.tar.gz
Source0:	%{name}-20020912.tar.gz
# Source0-md5:	345762a0de41b2a9782dbbec6e609020
Patch0:		%{name}-missing_assert_h.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	libuta-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is a UI library which is independent from the used widget
library. The base libary provides an abstract instance of a UI; any
dialog is described by a XML-stylish data structure and can be
executed by the dialog engine.

%description -l pl.UTF-8
To jest biblioteka interfejsu użytkownika niezależna od użytej
biblioteki widgetów. Podstawowa biblioteka daje abstrakcyjną instancję
interfejsu; każde okienko dialogowe jest opisane przez strukturę
danych w stylu XML i może być wykonane przez silnik dialogowy.

%package libuta
Summary:	Janus library - libuta bindings
Summary(pl.UTF-8):   Biblioteka Janus - interfejs do libuta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description libuta
This library is a UI library which is independent from the used widget
library. The base libary provides an abstract instance of a UI; any
dialog is described by a XML-stylish data structure and can be
executed by the dialog engine.

This package contains bindings for libuta.

%description libuta -l pl.UTF-8
To jest biblioteka interfejsu użytkownika niezależna od użytej
biblioteki widgetów. Podstawowa biblioteka daje abstrakcyjną instancję
interfejsu; każde okienko dialogowe jest opisane przez strukturę
danych w stylu XML i może być wykonane przez silnik dialogowy.

Ten pakiet zawiera interfejs do widgetów libuta.

%package gtk
Summary:	Janus library - GTK+ bindings
Summary(pl.UTF-8):   Biblioteka Janus - interfejs do GTK+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
This library is a UI library which is independent from the used widget
library. The base libary provides an abstract instance of a UI; any
dialog is described by a XML-stylish data structure and can be
executed by the dialog engine.

This package contains bindings for GTK+ library.

%description gtk -l pl.UTF-8
To jest biblioteka interfejsu użytkownika niezależna od użytej
biblioteki widgetów. Podstawowa biblioteka daje abstrakcyjną instancję
interfejsu; każde okienko dialogowe jest opisane przez strukturę
danych w stylu XML i może być wykonane przez silnik dialogowy.

Ten pakiet zawiera interfejs do widgetów GTK+.

%package devel
Summary:	Header files for janus development
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia programów z użyciem biblioteki Janus
Group:		Development/Libraries
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	%{name}-libuta = %{version}-%{release}
Requires:	gtk+-devel
Requires:	libuta-devel

%description devel
This library is a UI library which is independent from the used widget
library. The base libary provides an abstract instance of a UI; any
dialog is described by a XML-stylish data structure and can be
executed by the dialog engine.

This package contains the header files needed to develop programs that
use these janus library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne przy tworzeniu programów
z użyciem biblioteki Janus.

%package static
Summary:	Static libraries for janus development
Summary(pl.UTF-8):   Statyczne biblioteki Janus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This library is a UI library which is independent from the used widget
library. The base libary provides an abstract instance of a UI; any
dialog is described by a XML-stylish data structure and can be
executed by the dialog engine.

This package contains the static Janus libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki Janus.

%prep
%setup -q -n %{name}-0.4.5
%patch0

%build
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	libuta -p /sbin/ldconfig
%postun	libuta -p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libjanus.so.*.*

%files libuta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjanus_libuta.so.*.*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjanus_gtk.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/janus-config
%{_includedir}/janus
%{_libdir}/lib*.la
%{_aclocaldir}/janus.m4
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
