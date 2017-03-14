%{?scl:%scl_package nodejs-asap}
%{!?scl:%global pkg_name %{name}}

#tests are not included in the tarball
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-asap
Version:        2.0.5
Release:        1%{?dist}
Summary:    High-priority task queue for Node.js and browser
License:    MIT
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
cp -pr package.json *.js \
    %{buildroot}%{nodejs_sitelib}/asap

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
#npm run lint
%{?scl:scl enable %{scl} - << \EOF}
%{__nodejs} test/asap-test.js
%{?scl:EOF}
%endif

%files
%doc LICENSE.md README.md
%{nodejs_sitelib}/asap

%changelog
* Thu Jan 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.5-1
- Updated with script

* Tue Sep 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.4-1
- Update, add tests

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
