Summary:	GUI frontend for the Video4Linux functions of transcode
Summary(pl):	Graficzny frontend do funkcji Video4Linux konwertera transcode
Name:		gv4l
Version:	2.2.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gv4l/%{name}-%{version}.tar.gz
# Source0-md5:	f2f1e1261189e364f1e0cad8566c725c
URL:		http://gv4l.sourceforge.net/
Source1:	%{name}.desktop
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
Requires:	transcode >= 0.6.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gv4l is a GUI frontend for the v4l functions of transcode.

%description -l pl
Gv4l to graficzny frontend do funkcji Video4Linux konwertera
transcode.

%prep
%setup -q
#%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/gv4l.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
