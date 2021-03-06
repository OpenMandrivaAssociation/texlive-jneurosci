# revision 17346
# category Package
# catalog-ctan /biblio/bibtex/contrib/jneurosci
# catalog-date 2010-03-06 20:55:14 +0100
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-jneurosci
Version:	1.00
Release:	11
Summary:	BibTeX style for the Journal of Neuroscience
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/jneurosci
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jneurosci.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jneurosci.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a slightly modified version of the namedplus style,
which fully conforms with the Journal of Neuroscience citation
style. It should be characterised as an author-date citation
style; a BibTeX style and a LaTeX package are provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 752913
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 718755
- texlive-jneurosci
- texlive-jneurosci
- texlive-jneurosci
- texlive-jneurosci

