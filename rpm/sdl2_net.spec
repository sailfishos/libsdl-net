Summary: Simple DirectMedia Layer - Portable Network Library
Name: SDL2_net
Version: 2.2.0
Release: 1
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libsdl-org/SDL_net
License: zlib
BuildRequires: cmake
BuildRequires: pkgconfig(sdl2)
BuildRequires: autoconf
BuildRequires: automake

%description
This is a portable network library for use with SDL.

%package devel
Summary: Simple DirectMedia Layer - Portable Network Library (Development)
Requires: %{name}

%description devel
This is a portable network library for use with SDL.

This is the libraries and include files you can use to
develop SDL networked applications.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
mkdir -p build
pushd build
%cmake .. \
  -DCMAKE_BUILD_TYPE=Release
%make_build
popd

%install
pushd build
%make_install
rm -f %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.txt
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/*

