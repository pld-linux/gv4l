Summary:	GUI frontend for the Video4Linux functions of transcode
Summary(pl):	Graficzny frontend do funkcji Video4Linux konwertera transcode
Name:		gv4l
Version:	2.2.4
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gv4l/%{name}-%{version}.tar.gz
# Source0-md5:	b5692b64f78948d187e1a024f68c6d7f
URL:		http://gv4l.sourceforge.net/
Patch0:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.25
BuildRequires:	libgnomeui-devel
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/gv4l.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/%{name}.png
