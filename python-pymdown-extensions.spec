#
# Conditional build:
%bcond_without	doc	# MkDocs documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Extension pack for Python Markdown
Summary(pl.UTF-8):	Zestaw rozszerzeń do pakietu Python Markdown
Name:		python-pymdown-extensions
Version:	5.0
Release:	3
License:	MIT, BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pymdown-extensions/
Source0:	https://files.pythonhosted.org/packages/source/p/pymdown-extensions/pymdown-extensions-%{version}.tar.gz
# Source0-md5:	158931bf0b6eef56896743c0af1f5c19
URL:		https://github.com/facelessuser/pymdown-extensions
%if %{with doc}
BuildRequires:	python-mkdocs
BuildRequires:	python-mkdocs-material
%endif
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML >= 3.10
BuildRequires:	python-markdown >= 2.6.10
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 3.10
BuildRequires:	python3-markdown >= 2.6.10
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extension pack for Python Markdown.

%description -l pl.UTF-8
Zestaw rozszerzeń do pakietu Python Markdown.

%package -n python3-pymdown-extensions
Summary:	Extension pack for Python Markdown
Summary(pl.UTF-8):	Zestaw rozszerzeń do pakietu Python Markdown
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pymdown-extensions
Extension pack for Python Markdown.

%description -n python3-pymdown-extensions -l pl.UTF-8
Zestaw rozszerzeń do pakietu Python Markdown.

%package apidocs
Summary:	API documentation for Python pymdown-extensions module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pymdown-extensions
Group:		Documentation

%description apidocs
API documentation for Python pymdown-extensions module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pymdown-extensions.

%prep
%setup -q -n pymdown-extensions-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
mkdocs build --clean --verbose --strict

%{__rm} site/{__init__.py*,sitemap.xml*}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py_sitescriptdir}/pymdownx
%{py_sitescriptdir}/pymdown_extensions-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pymdown-extensions
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py3_sitescriptdir}/pymdownx
%{py3_sitescriptdir}/pymdown_extensions-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc site/*
%endif
