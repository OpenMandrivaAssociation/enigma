Summary: Enigma is a puzzle game
Name: enigma
Version: 1.03
Release: %mkrel 5
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

mkdir -p $RPM_BUILD_ROOT%{_menudir}

cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
	command="%{_bindir}/%{name}" \
	needs="x11" \
	section="Amusement/Boards" \
	title="Enigma" \
	icon="boards_section.png" \
	longtitle="Enigma is a puzzle game" \
	startup_notify="false" \
        xdg="true"
EOF

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

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/*
%{_datadir}/enigma
%{_menudir}/*
%{_datadir}/applications/mandriva-%{name}.desktop

