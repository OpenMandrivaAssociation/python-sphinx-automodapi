%define	module	sphinx-automodapi

Summary:	Sphinx extension to automatically generate API pages for whole modules
Name:		python-%{module}
Version:	0.22.0
Release:	1
#Source0:	https://github.com/astropy/sphinx-automodapi/archive/refs/tags/v%{version}.tar.gz
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_automodapi/sphinx_automodapi-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://sphinx-doc.org/
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	git-core

%description
HTML help file support for the Sphinx documentation generator.

%prep -a
# Make setuptools-scm happy
git init
git config user.email info@openmandriva.org
git config user.name "OpenMandriva Builder"
git add .
git commit -am "Import %{version}"
git tag -a %{version} -m %{version}

%files
%{py_puresitedir}/sphinx_automodapi
%{py_puresitedir}/sphinx_automodapi-%{version}.dist-info
