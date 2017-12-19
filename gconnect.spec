
%global commit a03927b525a78bf2fcee976f3116520bb0033fb3

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner nvlgit

%global __python %{__python3}

Name:           gconnect
Version:        0.1.0
Release:        2.20171021git%{shortcommit}%{?dist}
Summary:        Implementation of KDE Connect protocol

License:        GPLv3
URL:            http://github.com/getzze/gconnect
Source0:        https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  vala
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  json-glib-devel
BuildRequires:  libgee-devel
BuildRequires:  libpeas-devel
BuildRequires:  libnotify-devel
BuildRequires:  gnutls-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libuuid-devel
BuildRequires:  meson

BuildRequires:  gtk3-devel
BuildRequires:  caribou-devel
BuildRequires:  python3

Requires:       libnotify
Requires:       libgee
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}

%description
gconnect is an implementation of the KDE Connect protocol in Vala using GLib2.
Plugins can be written in Vala, C, Python or Lua using libpeas.

%package        lib
Summary:        %{name}-lib for %{name}

%description    lib
gconnect is an implementation of the KDE Connect protocol in Vala using GLib2.
Plugins can be written in Vala, C, Python or Lua using libpeas.
This package contains the library for %{name} and base plugins.

# Separate package to avoid Segmentation fault under Wayland
%package        mousepad-plugin
Summary:        %{name}-mousepad-plugin for %{name}
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}

%description    mousepad-plugin
This package contains mousepad-plugin for %{name}. 
%{name}-mousepad-plugin use direct x11 calls. It's not compatible with Wayland.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains development files for %{name}

%prep
%setup -q -D -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md HISTORY.md
%{_bindir}/%{name}d

%files lib
%{_libdir}/lib%{name}*.so
%{_libdir}/girepository*/*
%{_datadir}/%{name}/plugins/battery/*
%{_datadir}/%{name}/plugins/clipboard/*
%{_datadir}/%{name}/plugins/findmyphone/*
%{_datadir}/%{name}/plugins/mpriscontrol/*
%{_datadir}/%{name}/plugins/ping/*
%{_datadir}/%{name}/plugins/runcommand/*
%{_datadir}/%{name}/plugins/telephony/*
%{_datadir}/%{name}/plugins/*.py
%{_datadir}/glib-2.0/schemas/*.xml

%files mousepad-plugin
%{_datadir}/%{name}/plugins/mousepad/*

%files devel
%{_includedir}/%{name}*.h
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/vala/vapi/%{name}*.vapi
%{_datadir}/gir*/*.gir

%changelog
* Fri Dec 08 2017 - minor spec changes
- Move mousepad plugin to separate package

* Mon Dec 04 2017 - initial spec
- v0.1.0, commit 98189359fb1261d8e37d9786414958f8d454144b

