%global app_id  com.gitlab.nvlgit.Balss

Name:           Balss
Version:        0.1.0
Release:        1%{?dist}
Summary:        AudioBook player

License:        GPLv3
URL:            https://gitlab.com/nvlgit/Balss
Source0:        https://gitlab.com/nvlgit/%{name}/-/archive/master/%{name}-master.tar.gz

BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(mpv) >= 0.28
BuildRequires:  vala >= 0.40
BuildRequires:  meson >= 0.40
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
The %{name} is an easy to use player for audiobook files with chapters such as m4b or mka.


%prep
%autosetup -n %{name}-master

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{app_id}.desktop

%files
%license LICENSE
%doc README.md
%attr(755, root, root) %{_bindir}/%{app_id}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/appdata/%{app_id}.appdata.xml
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.svg
%{_datadir}/icons/hicolor/*/apps/%{app_id}-symbolic.svg



%changelog
* Thu Oct 11 2018 - 0.1.0
- initial spec
