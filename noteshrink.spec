
Name:           noteshrink
Version:        0.1.1
Release:        1%{?dist}
Summary:        Convert scans of handwritten notes to PDFs

License:        MIT
URL:            https://github.com/mzucker/noteshrink
Source0:        https://github.com/mzucker/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-rpm-macros

Requires:       python3-numpy >= 1.10
Requires:       python3-scipy
Requires:       ImageMagick
Requires:       python3-pillow

%description
The %{name} is tool for converting scans of handwritten notes to beautiful, compact PDFs

%prep
%autosetup -n %{name}-%{version}

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install --root=$RPM_BUILD_ROOT

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/*

%changelog
* Fri Apr 13 2018 - 0.1.1-1
- initial spec
