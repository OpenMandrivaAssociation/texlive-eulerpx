Name:		texlive-eulerpx
Version:	63967
Release:	2
Summary:	A modern interface for the Euler math fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eulerpx
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eulerpx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eulerpx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the "eulerpx" font, which started as a
hybrid of multiple other font packages, notably eulervm and
newpxmath. This package was put together with the intent to use
it with the Palatino and Optima fonts, but it may work with
other combinations, too.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/eulerpx
%doc %{_texmfdistdir}/doc/fonts/eulerpx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
