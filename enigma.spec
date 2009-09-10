Summary: Puzzle game
Name: enigma
Version: 1.03
Release: %mkrel 11
Source0: %{name}-%{version}.tar.bz2
Patch0: enigma-1.03-fix-install.patch
License: MIT
Group: Games/Puzzles
URL: http://www.chiark.greenend.org.uk/~sgtatham/enigma/
BuildRequires: ncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/*
%{_datadir}/enigma
%{_datadir}/applications/mandriva-%{name}.desktop
