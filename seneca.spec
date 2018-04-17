%global __python %{__python3}

%global commit 292733ddac246e37a8e06886ae4e2622cde164c0
%global date 20180210
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner dyskette


Name:           seneca
Version:        alpha2
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        epub reader

License:        GPLv3
URL:            https://github.com/dyskette/seneca
Source0:        https://github.com/%{owner}/%{name}/archive/%{name}-%{commit}.tar.gz

#BuildArch:     noarch
BuildRequires:  meson
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  pygobject3-devel
BuildRequires:  webkit2gtk3-devel

Requires:       python3-gobject
Requires:       python3-lxml
Requires:       webkit2gtk3

%description
The %{name} is an epub reader made to fit in GNOME.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%defattr(644,root,root)
%license COPYING
%doc README.md
%attr(755, root, root) %{_bindir}/%{name}
%{_libdir}/%{name}/webkitextension/*
%{_datadir}/applications/com.github.dyskette.Seneca.desktop
%{_datadir}/icons/hicolor/*/apps/com.github.dyskette.Seneca.svg
%{_datadir}/%{name}/*


%changelog
* Tue Apr 17 2018 - Alpha 2 version
- initial spec
