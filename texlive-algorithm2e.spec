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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

