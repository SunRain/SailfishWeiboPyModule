#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
#

Name:       sailfishweibopy
# >> macros
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
# << macros
%define sailfishweibo /usr/share/harbour-sailfish_sinaweibo
%define pycurl  /usr/share/doc/pycurl
Summary:    login module for SailfishWeibo
Version:    0.2
Release:    2
Group:      Python
License:    LGPL
URL:        https://github.com/SunRain/SailfishWeibo
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:   python3-devel
BuildRequires:   gcc
BuildRequires:	 libcurl-devel
BuildRequires:   openssl-devel
Requires:        openssl-libs
Requires:        libcurl


%description
This module provides Python bindings for the cURL library.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build

# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
export PYCURL_SSL_LIBRARY=openssl
#python3 -m pip install pycurl
cd pycurl-7.19.5.3 && python3 setup.py --with-ssl install --root $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{sailfishweibo}/qml/
cp -r $RPM_BUILD_DIR/qml/* %{buildroot}%{sailfishweibo}/qml/
# >> install post
# << install post

%pre
# >> pre
# << pre

%preun
# >> preun
# << preun
%postun
rm -rf /usr/lib/python3.4/site-packages/curl
rm -rf /usr/lib/python3.4/site-packages/pycurl*
%files
%defattr(-,root,root,-)
/usr/lib/python3.4/site-packages/*
%doc %{pycurl}/*
%{sailfishweibo}
# >> files
# << files

%changelog
* Mon Jan 18 2016 BirdZhang <0312birdzhang@gmail.com> 0.2-2
- 更改为sailfish客户端key
