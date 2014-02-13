Summary: Puzzle game
Name: enigma
Version: 1.20
Release: 1
Source0: http://downloads.sourceforge.net/enigma-game/Release%201.20/%{name}-%{version}.tar.gz
Patch0: enigma-1.03-fix-install.patch
License: MIT
Group: Games/Puzzles
URL: http://www.chiark.greenend.org.uk/~sgtatham/enigma/
BuildRequires: ncurses-devel

%description
Enigma is a puzzle game with elements of Boulderdash and elements 
of Sokoban, but is possibly most similar to the old Spectrum game XOR.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Enigma
Comment=Enigma is a puzzle game
Exec=%{_bindir}/%{name} 
Icon=puzzle_section
Terminal=true
Type=Application
StartupNotify=false
Categories=Game;LogicGame;
EOF

%files
%doc README 
%{_bindir}/*
%{_datadir}/enigma
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.03-12mdv2011.0
+ Revision: 618232
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.03-11mdv2010.0
+ Revision: 437465
- rebuild

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 1.03-10mdv2009.1
+ Revision: 364323
- fix install
- move to puzzle section

* Thu Apr 02 2009 Götz Waschk <waschk@mandriva.org> 1.03-9mdv2009.1
+ Revision: 363483
- fix menu entry (bug #49435)
- fix license

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.03-8mdv2009.0
+ Revision: 244909
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.03-6mdv2008.1
+ Revision: 170816
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- drop old menu

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.03-5mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import enigma


* Mon Sep 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.03-5mdv2007.0
- XDG

* Tue Jan 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1.03-4mdk
- Rebuild

* Wed Sep 03 2003 Michael Scherer <scherer.michael@free.fr> 1.03-3mdk
- BuildRequires ncurses-devel 

* Thu Aug 14 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.03-2mdk
- fix desc. and changelog to reflect what this package is (regarding the 
 enigma-freeoxyd that will be uploaded)

* Mon Mar 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.03-1mdk
- 1.03



