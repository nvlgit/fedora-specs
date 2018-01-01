%global commit 77bf6f82c6b718b628ea9b004adc4409242506c9

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner nvlgit


Name:           libvalce
Version:        3.0.1
Release:        1.20180101git%{shortcommit}%{?dist}
Summary:        libVLC GObject wrapper

License:        GPLv3      
URL:            https://github.com/nvlgit/libvalce
Source0:        https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  vlc-devel
BuildRequires:  meson

Requires:       vlc

%description
libvalce is a GObject based API wrapper for libVLC >= v3.0.0

%package        devel
Summary:        Development package for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       vlc-devel

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
%license LICENSE
%doc README.md
%{_libdir}/%{name}-*.so
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/%{name}/%{name}*.h
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/%{name}*.vapi
%{_datadir}/vala/vapi/%{name}*.deps

%changelog
* Mon Jun 01 2018 - 3.0.1-1
- initial spec
