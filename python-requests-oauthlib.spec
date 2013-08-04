%define		module	requests-oauthlib
Summary:	First-class OAuth library support for Requests
Name:		python-%{module}
Version:	0.3.2
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	https://github.com/requests/requests-oauthlib/archive/v%{version}.tar.gz
# Source0-md5:	8e2166f7a6f895df17420a6f35e30672
URL:		https://github.com/requests/requests-oauthlib
BuildRequires:	python-modules
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
Requires:	python-modules
Requires:	python-oauthlib
Requires:	python-requests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
First-class OAuth library support for Requests.

%package -n python3-requests-oauthlib
Summary:	First-class OAuth library support for Requests
Group:		Development/Languages/Python
Requires:	python3-modules
Requires:	python3-oauthlib
Requires:	python3-requests

%description -n python3-requests-oauthlib
First-class OAuth library support for Requests.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/requests_oauthlib

%files -n python3-requests-oauthlib
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/requests_oauthlib

