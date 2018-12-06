# https://github.com/buger/jsonparser/
%global goipath  github.com/buger/jsonparser
%global commit   52c6e1462ebdfb4f59765ca13bd8fa1c31b1d7eb

%global common_description %{expand:
Alternative JSON parser for Go (so far fastest)

It does not require you to know the structure of the payload (eg. create
structs), and allows accessing fields by providing the path to them. It is up to
10 times faster than standard encoding/json package (depending on payload size
and usage), allocates no memory.}

%gometa

Name: %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: Alternative JSON parser for Go that does not require schema (so far fastest)
License: MIT
URL: %{gourl}
Source0: %{gosource}

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%forgesetup
# remove test benchmarks of other JSON libraries to limit dependencies
rm benchmark/benchmark_{codecgen,easyjson,ffjson,{large,medium,small}_payload_test}.go

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Tue Nov 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181113git52c6e14
- Bump to commit 52c6e1462ebdfb4f59765ca13bd8fa1c31b1d7eb

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.3.20180322git2cac668
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git2cac668.git2cac668
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.20180322git2cac668
- First package for Fedora
