%global debug_package %{nil}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-zope-filesystem
Version:        1
Release:        5%{?dist}
Summary:        Python-Zope Libraries Base Filesystem
Group:          Development/Languages
License:        ZPLv2.1
URL:            https://fedoraproject.org/wiki/SIGs/SciTech/SAGE
Source0:        python-zope-filesystem-__init__.py
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel


%description
This package contains the base filesystem layout for all python-zope-* packages


%prep
%setup -q -c -T
cp -p %{SOURCE0} __init__.py


%build
# nothing


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}/zope
install -p -m 644 __init__.py $RPM_BUILD_ROOT%{python_sitelib}/zope
mkdir -p $RPM_BUILD_ROOT%{python_sitearch}/zope
install -p -m 644 __init__.py $RPM_BUILD_ROOT%{python_sitearch}/zope

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
# For noarch packages: sitelib
%{python_sitelib}/zope
%if "%{python_sitearch}" != "%{python_sitelib}"
# For arch-specific packages: sitearch
%{python_sitearch}/zope
%endif


%changelog
* Mon Jun 28 2010 David Malcolm <dmalcolm@redhat.com> - 1-5
- fix %%description
- use %%global rather than %%define
Resolves: rhbz#608091

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 1-2
- Don't list files twice on non-lib64 platforms.
- Preserve timestamps.

* Sun Dec 14 2008 Conrad Meyer <konrad@tylerc.org> - 1-1
- Initial package.
