
%global glib2_version 2.50
%global gtk3_version 3.22
%global gtk4_version 4.8
%global taglib_c_version 1.11
%global editor_name com.gitlab.nvlgit.metadata-editor


Name:           nautilus-metadata-editor-extension
Version:        43.0.1
Release:        1%{?dist}
Summary:        Metadata Editor Extension for the Nautilus file manager

Group:          User Interface/Desktops
License:        GPLv3
URL:            https://gitlab.com/nvlgit/nautilus-metadata-editor-extension
Source0:        https://gitlab.com/nvlgit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(taglib_c) >= %{taglib_c_version}
BuildRequires:  vala >= 0.40
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  gettext
BuildRequires:  meson

Requires:       taglib >= 1.11
Requires:       nautilus

%description
This extension adds Metadata Editor for audio/video files to the Nautilus file manager.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}

%check
%meson_test


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{editor_name}
%{_datadir}/applications/%{editor_name}.desktop
%{_libdir}/nautilus/extensions-4/lib%{name}.so


%changelog
* Sun Sep 18 2022 Nick
- update to 43.0.1

* Sun Jun 17 2018 Nick
- initial spec
