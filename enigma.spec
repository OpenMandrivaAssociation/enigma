Summary:	Puzzle game similar to Oxyd
Name:		enigma
Version:	1.20
Release:	2
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.nongnu.org/enigma/
Source0:	http://downloads.sourceforge.net/%{name}-game/Release%20%{version}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(xerces-c)

%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd.  Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape.  Sounds simple?  It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/enigma
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/pixmaps/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -rf %{buildroot}/%{_docdir}/%{name}

rm -rf %{buildroot}%{_includedir} %{buildroot}%{_libdir}/*.a

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="PuzzleGame" \
  --add-category="ArcadeGame;LogicGame" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

