%{?scl:%scl_package nodejs-asap}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-asap
Version:    1.0.0
Release:    5%{?dist}
Summary:    High-priority task queue for Node.js and browser
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/kriskowal/asap
Source0:    http://registry.npmjs.org/asap/-/asap-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires: %{?scl_prefix}nodejs

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/asap
cp -pr package.json asap.js \
    %{buildroot}%{nodejs_sitelib}/asap

%nodejs_symlink_deps

%files
%doc LICENSE.md README.md
%{nodejs_sitelib}/asap

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-5
- rebuilt

* Thu Nov 26 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-4
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- initial package
