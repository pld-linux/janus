Summary:	Janus library
Name:		janus
Version:	0.4.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://victor.worldforge.org/pub/worldforge/libs/janus/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuta-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is a UI library which is independent from the used
widget library.  The base libary provides an abstract instance
of a UI; any dialog is described by a XML-stylish data structure
and can be executed by the dialog engine. 

%package libuta
Summary:	Janus library - libuta bindings
Group:		Libraries
Requires:	%{name} = %{version}

%description libuta
This library is a UI library which is independent from the used
widget library.  The base libary provides an abstract instance
of a UI; any dialog is described by a XML-stylish data structure
and can be executed by the dialog engine. 

This package contains bindings for libuta

%package gtk
Summary:	Janus library - gtk bindings
Group:		Libraries
Requires:	%{name} = %{version}

%description gtk
This library is a UI library which is independent from the used
widget library.  The base libary provides an abstract instance
of a UI; any dialog is described by a XML-stylish data structure
and can be executed by the dialog engine. 

This package contains bindings for gtk library.

%package devel
Summary:	Header files and libraries for janus development
Group:		Development/Libraries
Requires:	%{name}-gtk = %{version}
Requires:	%{name}-libuta = %{version}
Requires:	libuta-devel
Requires:	gtk+-devel

%description devel
This library is a UI library which is independent from the used
widget library.  The base libary provides an abstract instance
of a UI; any dialog is described by a XML-stylish data structure
and can be executed by the dialog engine. 

This package contains the header files needed to develop programs that
use these janus library.

%package static
Summary:	Static libraries for janus development
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This library is a UI library which is independent from the used
widget library.  The base libary provides an abstract instance
of a UI; any dialog is described by a XML-stylish data structure
and can be executed by the dialog engine. 

This package contains the static libuta.

%prep
%setup -q

%build
aclocal
autoheader
libtoolize --automake --copy --force
automake --add-missing --copy --gnu --force
autoconf
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/libjanus.so.0
%attr(755,root,root) %{_libdir}/libjanus.so.*.*

%files libuta
%defattr(644,root,root,755)
%{_libdir}/libjanus_libuta.so.0
%attr(755,root,root) %{_libdir}/libjanus_libuta.so.*.*

%files gtk
%defattr(644,root,root,755)
%{_libdir}/libjanus_gtk.so.0
%attr(755,root,root) %{_libdir}/libjanus_gtk.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/janus-config
%{_includedir}/janus
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
