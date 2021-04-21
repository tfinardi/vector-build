%define datadir /var/lib/vector/
Name:		vector
Version:	0.12.2
Release:	0
Summary:	Vector is a high-performance, end-to-end (agent & aggregator) observability data platform that puts you in control of your observability data.
License:	Mozilla Public License 2.0
URL:		https://github.com/timberio/vector
Source:	https://github.com/tfinardi/vector-build/blob/main/SOURCES/vector-0.12.2.tar.gz
BuildArch:	x86_64

%description
Vector is a high-performance, end-to-end (agent & aggregator) observability data platform that puts you in control of your observability data.

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT
cp -R * $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0644,root,root)/etc/vector/vector.toml
%attr(0755,root,root)/usr/bin/vector
%attr(0755,root,root)/etc/systemd/system/vector.service
%attr(0755,root,root)/var/lib/vector

%changelog
* Mon Mar 29 2021 <thiago.finardi@azion.com> - 0.12.2-0
- This release includes a few critical bug fixes and a an update to OpenSSL to 1.1.1k resolve CVE-2021-3450 and CVE-2021-3449.

