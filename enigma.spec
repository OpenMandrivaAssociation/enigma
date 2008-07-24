Summary: Puzzle game
Name: enigma
Version: 1.03
Release: %mkrel 8
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Games/Boards
URL: http://www.chiark.greenend.org.uk/~sgtatham/enigma/
BuildRequires: ncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Enigma is a puzzle game with elements of Boulderdash and elements 
of Sokoban, but is possibly most similar to the old Spectrum game XOR.

%prep
%setup -q

%build

%configure

%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%_bindir

%makeinstall



mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Enigma
Comment=Enigma is a puzzle game
Exec=%{_bindir}/%{name} 
Icon=boards_section
Terminal=false
Type=Application
StartupNotify=false
Categories=X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/*
%{_datadir}/enigma
%{_datadir}/applications/mandriva-%{name}.desktop

