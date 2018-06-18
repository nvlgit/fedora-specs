
%global nautilus_version 3.28
%global glib2_version 2.50
%global gtk3_version 3.22
%global taglib_c_version 1.11


Name:           nautilus-metadata-editor-extension
Version:        3.28.0
Release:        1%{?dist}
Summary:        Metadata Editor Extension for the Nautilus file manager

Group:          User Interface/Desktops
License:        GPLv3
URL:            https://gitlab.com/nvlgit/nautilus-metadata-editor-extension
Source0:        %{name}-%{version}.tar.xz


BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(taglib_c) >= %{taglib_c_version}
BuildRequires:  vala >= 0.40
BuildRequires:  pkgconfig(libnautilus-extension) >= %{nautilus_version}
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  gettext
BuildRequires:  meson

Requires:       taglib >= 1.11
Requires:       nautilus >= %{nautilus_version}

%description
This extension adds Metadata Editor for audio files to the Nautilus file manager.


%prep
%autosetup -n %{name}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE
%doc README.md
%{_bindir}/com.gitlab.nvlgit.metadata-editor
%{_datadir}/applications/com.gitlab.nvlgit.metadata-editor.desktop
%{_libdir}/nautilus/extensions-3.0/lib%{name}.so


%changelog
* Sun Jun 17 2018 initial spec
- 
