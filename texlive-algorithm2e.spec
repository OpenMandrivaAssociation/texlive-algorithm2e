%global tl_name algorithm2e
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.2
Release:	%{tl_revision}.1
Summary:	Floating algorithm environment with algorithmic keywords
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algorithm2e
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithm2e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithm2e.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Algorithm2e is an environment for writing algorithms. An algorithm
becomes a floating object (like figure, table, etc.). The package
provides macros that allow you to create different keywords, and a set
of predefined key words is provided; you can change the typography of
the keywords. The package allows vertical lines delimiting a block of
instructions in an algorithm, and defines different sorts of algorithms
such as Procedure or Function; the name of these functions may be reused
in the text or in other algorithms.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/algorithm2e
%dir %{_datadir}/texmf-dist/tex/latex/algorithm2e
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/README
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e.pdf
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_ex01.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_ex02.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_ex03.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_ex04.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_ex05.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_ex06.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_ex07.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exAlgoDisjdecomp.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exIR.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exProg.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exfor.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exgeneric.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exgeneric2.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exnlsty.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exrepeat.tex
%doc %{_datadir}/texmf-dist/doc/latex/algorithm2e/algorithm2e_exswitch.tex
%{_datadir}/texmf-dist/tex/latex/algorithm2e/algorithm2e.sty
