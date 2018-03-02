Name:           nouveau-firmware
Version:        340.32
Release:        1%{?dist}
Summary:        Proprietary NVIDIA firmware

License:        Proprietary
URL:            https://nouveau.freedesktop.org/wiki/VideoAcceleration/
Source0:        http://us.download.nvidia.com/XFree86/Linux-x86/%{version}/NVIDIA-Linux-x86-%{version}.run
Source1:	https://raw.github.com/imirkin/re-vp2/master/extract_firmware.py

BuildRequires:  python2

%description
This package provides video & pgraph firmwares
extracted from proprietary NVIDIA-Linux-x86-%{version}.run

%prep


%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/usr/lib/nouveau/
cp -d %{SOURCE0} %{buildroot}/usr/lib/nouveau/
cp -d %{SOURCE1} %{buildroot}/usr/lib/nouveau/
cd %{buildroot}/usr/lib/nouveau/

sh NVIDIA-Linux-x86-%{version}.run --extract-only
python2 extract_firmware.py

rm -r -f NVIDIA-Linux-x86-%{version}.run
rm -r -f NVIDIA-Linux-x86-%{version}
rm -r -f extract_firmware.py


%files
%attr(0755, root, root) /usr/lib/nouveau/nv*
%attr(0755, root, root) /usr/lib/nouveau/vuc-*



%changelog
* Fri Mar  2 2018 initial spec
- 
