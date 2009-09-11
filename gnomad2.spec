%define	name	gnomad2
%define	version	2.9.4
%define rel	2
%define	release	%mkrel %{rel}
%define	Summary	A Nomad Jukebox manager

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
URL:		http://gnomad2.sourceforge.net/
Group:		Sound
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-0.9.4-fix-str-fmt.patch
BuildRequires:	libnjb-devel >= 2.2 
BuildRequires:	libgtk+2-devel
BuildRequires:	libid3tag-devel
BuildRequires:	imagemagick
BuildRequires:  perl-XML-Parser
BuildRequires:  desktop-file-utils
BuildRequires:  libmtp-devel >= 0.3.0
BuildRequires:  taglib-devel
BuildRequires:	hal-devel
BuildRequires:	dbus-devel
BuildRequires:	intltool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gnomad 2 is a GUI built on top of GTK/GNOME 2, libid3tag and libnjb that
makes it possible to transfer tracks and files from/to a
Creative Nomad Jukebox (all brands). It is designed much like
an ordinary graphical FTP program.

%prep
%setup -q
%patch0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

install -d %{buildroot}{%{_miconsdir},%{_liconsdir},%{_menudir}}
convert -size 16x16 %{name}-logo.png %{buildroot}%{_miconsdir}/%{name}-logo.png
convert -size 32x32 %{name}-logo.png %{buildroot}%{_iconsdir}/%{name}-logo.png
convert -size 48x48 %{name}-logo.png %{buildroot}%{_liconsdir}/%{name}-logo.png

perl -pi -e 's,%{name}-logo.png,%{name}-logo,g' %{buildroot}%{_datadir}/applications/*

%find_lang %{name}
desktop-file-install --vendor="" \
    --remove-category="Application" \
    --add-category="AudioVideo;Audio" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
	  
%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(755,root,root,755)
%{_bindir}/%{name}
%defattr(644,root,root,755)
%{_mandir}/man1/%{name}.1*
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-logo.png
%{_miconsdir}/%{name}-logo.png
%{_iconsdir}/%{name}-logo.png
%{_liconsdir}/%{name}-logo.png
%doc AUTHORS NEWS ChangeLog README TODO
