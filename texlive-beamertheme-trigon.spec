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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon
%dir %{_datadir}/texmf-dist/source/latex/beamertheme-trigon
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-trigon
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/frames.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/library.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/trigon_demo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/trigon_demo.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/trigon_full.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/trigon_small.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-trigon/trigontheme.pdf
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/Makefile
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/beamercolorthemetrigon.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/beamerfontthemetrigon.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/beamerinnerthemetrigon.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/beamerouterthemetrigon.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/beamerthemetrigon.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/beamerthemetrigon.ins
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-trigon/trigontheme.dtx
%{_datadir}/texmf-dist/tex/latex/beamertheme-trigon/beamercolorthemetrigon.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-trigon/beamerfontthemetrigon.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-trigon/beamerinnerthemetrigon.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-trigon/beamerouterthemetrigon.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-trigon/beamerthemetrigon.sty
