# %%global will not work here, lazy evaluation needed.
%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-mscore-fonts
Version:        2.2
Release:        5%{?dist}
Summary:        Bootstrap package building mscore-fonts using lpf

License:        MIT
URL:            https://github.com/leamas/lpf
Group:          Development/Tools
BuildArch:      noarch
Source0:        mscore-fonts.spec.in
Source1:        Licen.TXT
Source2:        61-ms-core-arial.conf
Source3:        61-ms-core-andale.conf
Source4:        61-ms-core-comic.conf
Source5:        61-ms-core-courier.conf
Source6:        61-ms-core-georgia.conf
Source7:        61-ms-core-impact.conf
Source8:        61-ms-core-times.conf
Source9:        61-ms-core-trebuchet.conf
Source10:       61-ms-core-verdana.conf
Source11:       61-ms-core-webdings.conf

BuildRequires:  desktop-file-utils
BuildRequires:  lpf
Requires:       lpf


%description
Bootstrap package allowing the lpf system to build the
mscore-fonts non-redistributable package.


%prep
%setup -cT


%build


%install
# lpf-setup-pkg [-e eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg -e %{SOURCE1} %{buildroot} %{SOURCE0} \
    %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
    %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11}


%post
%lpf_post

%postun
%lpf_postun

%lpf_triggerpostun


%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}


%changelog
* Sun Nov 07 2021 Sérgio Basto <sergio@serjux.com> - 2.2-5
- Add Obsoletes: old font names

* Wed May 26 2021 Sérgio Basto <sergio@serjux.com> - 2.2-4
- Rename packages from mscore-fonts ms-core-fonts

* Wed Dec 25 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.2-3
- Convert Licen.TXT file to UTF-8 encoding and Unix (CR) line-endings.

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 14 2014 Alec Leamas <leamas.alec@gmail.com> - 2.2-1
- New target spec: new description, lower priority.

* Mon Feb 10 2014 Alec Leamas <leamas.alec@gmail.com> - 2.2-1
- Initial release
