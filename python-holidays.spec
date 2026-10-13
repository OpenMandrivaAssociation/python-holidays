Name:		python-holidays
Version:	0.106
Release:	1
Summary:	Open World Holidays Framework
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/holidays/
Source0:	https://files.pythonhosted.org/packages/source/h/holidays/holidays-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildArch:	noarch
%description
Open World Holidays Framework.

%files
%{py_sitedir}/*
%{_bindir}/holidays-ics
