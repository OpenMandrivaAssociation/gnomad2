%define	name	gnomad2
%define	version	2.8.12
%define rel	1
%define	release	%mkrel %{rel}
%define	Summary	A Nomad Jukebox manager

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://gnomad2.sourceforge.net/
Group:		Sound
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	libnjb-devel >= 2.2 
BuildRequires:	libgtk+2-devel
BuildRequires:	libid3tag-devel
BuildRequires:	ImageMagick
BuildRequires:  perl-XML-Parser
BuildRequires:  desktop-file-utils
BuildRequires:  libmtp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gnomad 2 is a GUI built on top of GTK/GNOME 2, libid3tag and libnjb that
makes it possible to transfer tracks and files from/to a
Creative Nomad Jukebox (all brands). It is designed much like
an ordinary graphical FTP program.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

install -d $RPM_BUILD_ROOT{%{_miconsdir},%{_liconsdir},%{_menudir}}
convert -size 16x16 %{name}-logo.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}-logo.png
convert -size 32x32 %{name}-logo.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}-logo.png
convert -size 48x48 %{name}-logo.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}-logo.png

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}-logo.png" needs="x11" title="Gnomad 2" longtitle="A tool for managing Creative Nomad/Zen Jukeboxes and Dell DJs" section="Multimedia/Sound" xdg="true"
EOF


%find_lang %{name}
desktop-file-install --vendor="" \
    --remove-category="Application" \
    --add-category="X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio" \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
	  
%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_menudir}/%{name}
%doc AUTHORS NEWS ChangeLog README TODO


