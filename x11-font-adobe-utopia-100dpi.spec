Name: x11-font-adobe-utopia-100dpi
Version: 1.0.1
Release: %mkrel 4
Summary: Xorg X11 font adobe-utopia-100dpi
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-adobe-utopia-100dpi-%{version}.tar.bz2
License: CHECK
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-100dpi-fonts <= 6.9.0
PreReq: mkfontdir
PreReq: mkfontscale

%description
Xorg X11 font adobe-utopia-100dpi

%prep
%setup -q -n font-adobe-utopia-100dpi-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/100dpi

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/100dpi/fonts.dir
rm -f %{buildroot}%_datadir/fonts/100dpi/fonts.scale

%post
mkfontscale %_datadir/fonts/100dpi
mkfontdir %_datadir/fonts/100dpi

%postun
mkfontscale %_datadir/fonts/100dpi
mkfontdir %_datadir/fonts/100dpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_datadir/fonts/100dpi/UT*.pcf.gz


