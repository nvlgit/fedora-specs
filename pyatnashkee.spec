%global debug_package   %{nil}
%global app_id   com.gitlab.nvlgit.pyatnashkee
%global gtk3_version 3.22

Name:           pyatnashkee
Version:        0.1.0
Release:        2%{?dist}
Summary:        15-puzzle

License:        GPLv3      
URL:            https://gitlab.com/nvlgit/pyatnashkee
Source0:        https://gitlab.com/nvlgit/pyatnashkee/-/archive/master/pyatnashkee-master.tar.gz

BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  vala >= 0.40
BuildRequires:  meson >= 0.40

Requires:       gtk3 >= %{gtk3_version}

%description
A classic 15-puzzle game 


%prep
%setup -n %{name}-master


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{app_id}


%check
%meson_test
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{app_id}.desktop


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{app_id}.lang
%license COPYING
%doc README.md
%{_bindir}/%{app_id}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/*.svg


%changelog
* Sat Jun 23 2018 - 0.1.0-2
- complete app

* Mon Sep 25 2017 - 0.1.0-1
- jump to meson

* Sat Jun 10 2017 - 0.1.0-0
- initial spec
