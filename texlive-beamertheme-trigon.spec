Name:		texlive-beamertheme-trigon
Version:	65985
Release:	1
Summary:	A modern, elegant, and versatile theme for Beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-trigon
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-trigon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-trigon.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-trigon.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a modern, elegant and versatile theme for
Beamer, with a high degree of customization. Trigon found its
origin and inspiration in the graphical guidelines resulting
from the visual identity overhaul of the University of Liege.
Although directly inspired from these guidelines, the theme was
stripped out of any mention or specificities related to the
University and its faculties. This makes the Trigon theme
perfectly suitable for many different contexts. The final
product provides a modern, elegant and versatile theme with a
high degree of customization. The main design focuses on
triangular shapes for major layout elements and noise
minimization for the main body of the work. The theme's
implementation is heavily inspired from the Metropolis theme.
Most options from Metropolis have been ported to Trigon in
order to improve customization and ease-of-use. Trigon also
includes different styles and layouts for the main title page,
the section page and the default slide background.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beamertheme-trigon
%{_texmfdistdir}/tex/latex/beamertheme-trigon
%doc %{_texmfdistdir}/doc/latex/beamertheme-trigon

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
