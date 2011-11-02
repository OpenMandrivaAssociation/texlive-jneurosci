Name:		texlive-jneurosci
Version:	1.00
Release:	1
Summary:	BibTeX style for the Journal of Neuroscience
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/jneurosci
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jneurosci.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jneurosci.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a slightly modified version of the namedplus style,
which fully conforms with the Journal of Neuroscience citation
style. It should be characterised as an author-date citation
style; a BibTeX style and a LaTeX package are provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/jneurosci/jneurosci.bst
%{_texmfdistdir}/tex/latex/jneurosci/jneurosci.sty
%doc %{_texmfdistdir}/doc/latex/jneurosci/README
%doc %{_texmfdistdir}/doc/latex/jneurosci/jneurosci.pdf
%doc %{_texmfdistdir}/doc/latex/jneurosci/jneurosci.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
