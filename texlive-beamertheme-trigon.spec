%global tl_name beamertheme-trigon
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.0
Release:	%{tl_revision}.1
Summary:	A modern, elegant, and versatile theme for Beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-trigon
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-trigon.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-trigon.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-trigon.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a modern, elegant and versatile theme for Beamer,
with a high degree of customization. Trigon found its origin and
inspiration in the graphical guidelines resulting from the visual
identity overhaul of the University of Liege. Although directly inspired
from these guidelines, the theme was stripped out of any mention or
specificities related to the University and its faculties. This makes
the Trigon theme perfectly suitable for many different contexts. The
final product provides a modern, elegant and versatile theme with a high
degree of customization. The main design focuses on triangular shapes
for major layout elements and noise minimization for the main body of
the work. The theme's implementation is heavily inspired from the
Metropolis theme. Most options from Metropolis have been ported to
Trigon in order to improve customization and ease-of-use. Trigon also
includes different styles and layouts for the main title page, the
section page and the default slide background.

