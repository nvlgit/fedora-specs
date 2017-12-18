
%global commit 71b6ac0f57d325b55d5efd85f88391370d49ed40
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner nvlgit


Name:           headphones-plug-controller
Version:        0.1.0
Release:        1.20171217git%{shortcommit}%{?dist}
Summary:        Headphones plug detector with playback control

License:        MIT      
URL:            https://github.com/nvlgit/headphones-plug-controller
Source0:        https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  glib2-devel
BuildRequires:  pulseaudio-libs-devel
%{?systemd_requires}
BuildRequires:  systemd

Requires:       pulseaudio

%description
This program detects when you plug out your headphones and pauses music for you. When you plug them in again, it resumes all the players that were paused by this program.

%prep
%setup -q -D -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
* Mon Dec 18 2017 initial spec
- 
