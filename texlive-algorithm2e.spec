# revision 16417
# category Package
# catalog-ctan /macros/latex/contrib/algorithm2e
# catalog-date 2009-12-15 18:51:03 +0100
# catalog-license lppl
# catalog-version 4.01
Name:		texlive-algorithm2e
Version:	4.01
Release:	1
Summary:	Floating algorithm environment with algorithmic keywords
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/algorithm2e
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithm2e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithm2e.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Algorithm2e is an environment for writing algorithms. An
algorithm becomes a floating object (like figure, table, etc.).
The package provides macros that allow you to create different
keywords, and a set of predefined key words is provided; you
can change the typography of the keywords. The package allows
vertical lines delimiting a block of instructions in an
algorithm, and defines different sorts of algorithms such as
Procedure or Function; the name of these functions may be
reused in the text or in other algorithms.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/algorithm2e/algorithm2e.sty
%doc %{_texmfdistdir}/doc/latex/algorithm2e/README
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e.pdf
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_ex01.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_ex02.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_ex03.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_ex04.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_ex05.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_ex06.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_ex07.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_exAlgoDisjdecomp.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_exIR.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_exfor.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_exrepeat.tex
%doc %{_texmfdistdir}/doc/latex/algorithm2e/algorithm2e_exswitch.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
