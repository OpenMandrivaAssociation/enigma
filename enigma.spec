Summary:	Puzzle game similar to Oxyd
Name:		enigma
Version:	1.30
Release:	1
License:	GPL-2.0-or-later
Group:		Games/Arcade
URL:		https://www.nongnu.org/enigma/
Source0:	https://github.com/Enigma-Game/Enigma/releases/download/%{version}/Enigma-%{version}-src.tar.gz
Patch0:		enigma-1.30-format-security.patch
# Current autoconf adds -std=gnu23 to CC. Bundled Lua is compiled with
# "cc -x c++", and clang rejects -std=gnu23 together with -x c++.
%global		_disable_rebuild_configure 1
BuildSystem:	autotools
BuildOption:	--with-system-enet
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libenet)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(xerces-c)
BuildRequires:	pkgconfig(zlib)

%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd.  Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape.  Sounds simple?  It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

%install -a
desktop-file-install \
	--remove-key=Version \
	--remove-category=Application \
	--remove-category=PuzzleGame \
	--add-category=ArcadeGame \
	--add-category=LogicGame \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Catalogs are .po files under %%{_datadir}/enigma, so %%find_lang has nothing to list.
%files
%{_bindir}/enigma
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/pixmaps/*
%{_datadir}/enigma
%{_docdir}/enigma
