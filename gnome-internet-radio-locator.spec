Name:           gnome-internet-radio-locator
Version:        1.3.0
Release:        1%{?dist}
Summary:        GNOME Internet Radio Locator for GNOME 3
License:        GPLv3+
URL:            https://www.gnome.org/~ole/%{name}
Source:         %{url}/%{name}-%{version}.tar.xz

#BuildRequires:  gtk3-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pango
#BuildRequires:  libchamplain-devel
BuildRequires:  pkgconfig(champlain-0.12)
#BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  intltool
BuildRequires:  itstool
#BuildRequires:  libappstream-glib
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:  desktop-file-utils
#BuildRequires:  geocode-glib-devel
BuildRequires:  pkgconfig(geocode-glib-1.0)
#BuildRequires:  gstreamer-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
#BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
#BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
Requires:       gstreamer1 >= 1.8.3
Requires:       gstreamer1-plugins-ugly-free >= 1.8.3
Requires:       geocode-glib

%description
GNOME Internet Radio Locator for GNOME 3 is a Free Software program
that allows you to easily locate and listen to Free Internet Radio
stations by broadcasters on the Internet with the help of a map.

GNOME Internet Radio Locator for GNOME 3 is developed on the GNOME
3 platform and it requires gstreamer 1.0 for playback.

Enjoy Free Internet Radio.

%prep
%setup -q

%build
%configure --with-recording --disable-silent-rules --disable-schemas

%install
%make_install
%find_lang %{name} --with-man

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%post
%files -f %{name}.lang
%doc AUTHORS DEBIAN NEWS README TODO ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_bindir}/gnome-internet-radio-locator
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Sun May 20 2018 Ole Aamot <ole@gnome.org> - 1.3.0-0
- gnome-internet-radio-locator 1.3.0 build on Fedora Linux 28

* Sat May 19 2018 Ole Aamot <ole@gnome.org> - 1.2.0-0
- gnome-internet-radio-locator 1.2.0 build on Fedora Linux 28

* Fri Apr 27 2018 Ole Aamot <ole@gnome.org> - 1.1.3-1
- gnome-internet-radio-locator 1.1.3 build on Fedora Linux 28

* Fri Apr 27 2018 Ole Aamot <ole@gnome.org> - 1.1.2-1
- gnome-internet-radio-locator 1.1.2 build on Fedora Linux 28

* Sun Apr 22 2018 Ole Aamot <ole@gnome.org> - 1.1.1-1
- gnome-internet-radio-locator 1.1.1 build on Fedora Linux 27

* Sat Apr 21 2018 Ole Aamot <ole@gnome.org> - 1.1.0-1
- gnome-internet-radio-locator 1.1.0 build on Fedora Linux 27

* Sat Nov 25 2017 Ole Aamot <ole@gnome.org> - 1.0.2-1
- gnome-internet-radio-locator 1.0.2 build on Fedora Linux 26

* Mon Oct 23 2017 Ole Aamot <ole@gnome.org> - 1.0.1-1
- gnome-internet-radio-locator 1.0.1 build on Fedora Linux 26

* Sat Sep 16 2017 Ole Aamot <ole@gnome.org> - 1.0.0-1
- gnome-internet-radio-locator 1.0.0 build on Fedora Linux 26

* Sat Sep 02 2017 Ole Aamot <ole@gnome.org> - 0.9.0-1
- gnome-internet-radio-locator 0.9.0 build on Fedora Linux 26

* Sat Aug 12 2017 Ole Aamot <ole@gnome.org> - 0.8.0-1
- gnome-internet-radio-locator 0.8.0 build on Fedora Linux 26

* Fri Aug 04 2017 Ole Aamot <ole@gnome.org> - 0.7.0-1
- gnome-internet-radio-locator 0.7.0 build on Fedora Linux 26

* Wed Aug 02 2017 Ole Aamot <ole@gnome.org> - 0.6.2-1
- gnome-internet-radio-locator 0.6.2 build on Fedora Linux 26

* Tue Aug 01 2017 Ole Aamot <ole@gnome.org> - 0.6.1-1
- gnome-internet-radio-locator 0.6.1 build on Fedora Linux 26

* Wed Jul 19 2017 Ole Aamot <ole@gnome.org> - 0.6.0-1
- gnome-internet-radio-locator 0.6.0 build on Fedora Linux 25

* Tue Jul 18 2017 Ole Aamot <ole@gnome.org> - 0.5.3-1
- gnome-internet-radio-locator 0.5.3 build on Fedora Linux 25

* Tue Jul 18 2017 Ole Aamot <ole@gnome.org> - 0.5.2-1
- gnome-internet-radio-locator 0.5.2 build on Fedora Linux 25

* Mon Jul 17 2017 Ole Aamot <ole@gnome.org> - 0.5.1-1
- gnome-internet-radio-locator 0.5.1 build on Fedora Linux 25

* Sun Jul 09 2017 Ole Aamot <ole@gnome.org> - 0.5.0-1
- gnome-internet-radio-locator 0.5.0 build on Fedora Linux 25

* Tue Jun 27 2017 Ole Aamot <ole@gnome.org> - 0.4.0-1
- gnome-internet-radio-locator 0.4.0 build on Fedora Linux 25

* Sun Jun 18 2017 Ole Aamot <ole@gnome.org> - 0.3.0-1
- gnome-internet-radio-locator 0.3.0 build on Fedora Linux 25

* Sat Jun 17 2017 Ole Aamot <ole@gnome.org> - 0.2.1-1
- gnome-internet-radio-locator 0.2.1 build on Fedora Linux 25

* Fri Jun 16 2017 Ole Aamot <ole@gnome.org> - 0.2.0-1
- gnome-internet-radio-locator 0.2.0 build on Fedora Linux 25

* Thu Apr 27 2017 Ole Aamot <ole@gnome.org> - 0.1.2-1
- gnome-internet-radio-locator 0.1.2 build on Fedora Linux 25

* Thu Apr 27 2017 Ole Aamot <ole@gnome.org> - 0.1.1-1
- gnome-internet-radio-locator 0.1.1 build on Fedora Linux 25

* Wed Apr 26 2017 Ole Aamot <ole@gnome.org> - 0.1.0-1
- gnome-internet-radio-locator 0.1.0 build on Fedora Linux 25
