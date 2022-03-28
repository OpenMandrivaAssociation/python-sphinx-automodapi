%define	module	sphinx-automodapi

Summary:	Sphinx extension to automatically generate API pages for whole modules
Name:		python-%{module}
Version:	0.14.1
Release:	1
Source0:	https://github.com/astropy/%{module}/archive/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		http://sphinx-doc.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools

%description
HTML help file support for the Sphinx documentation generator.

%prep
%autosetup -n  %{module}-%{version} -p1

%build
%py_build

%install
%py_install

%files
%{py_puresitedir}/sphinx_automodapi
%{py_puresitedir}/sphinx_automodapi*.egg-info
