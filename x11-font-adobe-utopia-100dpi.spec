Name:		x11-font-adobe-utopia-100dpi
Version:	1.0.4
Release:	4
Summary:	Xorg X11 font adobe-utopia-100dpi
Group:		Development/X11
URL:	https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-adobe-utopia-100dpi-%{version}.tar.bz2
# License doesn't say we can modify the software
License:	Adobe Utopia
BuildArch:	noarch
BuildRequires:	x11-font-util >= 1.2
BuildRequires:	x11-util-macros >= 1.0.1
Conflicts:	xorg-x11-100dpi-fonts <= 6.9.0
Requires(post):	mkfontdir
Requires(postun):	mkfontdir
Requires(post):	mkfontscale
Requires(postun):	mkfontscale

%description
Xorg X11 font adobe-utopia-100dpi.

%prep
%setup -q -n font-adobe-utopia-100dpi-%{version}

%build
./configure --prefix=/usr --x-includes=%{_includedir}\
	    --x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/100dpi

%make

%install
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/100dpi/fonts.dir
rm -f %{buildroot}%_datadir/fonts/100dpi/fonts.scale

%post
mkfontscale %_datadir/fonts/100dpi
mkfontdir %_datadir/fonts/100dpi

%postun
mkfontscale %_datadir/fonts/100dpi
mkfontdir %_datadir/fonts/100dpi

%files
%doc COPYING
%_datadir/fonts/100dpi/UT*.pcf.gz
