Summary:	Gui frontend for the Video4Linux functions of transcode
Name:		gv4l
Version:	2.0
Release:	0.pre8
License:	GPL
Group:		X11/Applications
Source0:	http://warderx.ath.cx:81/projects/%{name}-%{version}.-8.tar.gz
Patch0:		%{name}-install.patch
URL:		http://warderx.ath.cx:81/projects/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	intltool >= 0.25
BuildRequires:	gtk+2-devel
Requires:	transcode >= 0.6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gv4l is a gui frontend for the v4l functions of transcode.

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
