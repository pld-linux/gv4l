Summary:	GUI frontend for the Video4Linux functions of transcode
Summary(pl):	Graficzny frontend do funkcji Video4Linux konwertera transcode
Name:		gv4l
Version:	2.0
Release:	0.pre8.1
License:	GPL
Group:		X11/Applications
Source0:	http://warderx.ath.cx:81/projects/%{name}-%{version}.-8.tar.gz
# Source0-md5:	c870241f42b05a1e8a455e06c6078c2d
Patch0:		%{name}-install.patch
URL:		http://warderx.ath.cx:81/projects/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
Requires:	transcode >= 0.6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gv4l is a GUI frontend for the v4l functions of transcode.

%description -l pl
Gv4l to graficzny frontend do funkcji Video4Linux konwertera
transcode.

%prep
%setup -q -n %{name}-%{version}.-8
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# temporary desktop files fix
echo "Categories=Application;AudioVideo;Merged;" >> $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
echo "Categories=Application;AudioVideo;Merged;" >> $RPM_BUILD_ROOT%{_desktopdir}/%{name}1.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/%{name}
