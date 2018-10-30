Name:		texlive-algorithm2e
Version:	5.2
Release:	3
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
%{_texmfdistdir}/tex/latex/algorithm2e
%doc %{_texmfdistdir}/doc/latex/algorithm2e

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
