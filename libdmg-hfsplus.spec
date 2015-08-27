Name:		libdmg-hfsplus
Version:	c3ea1b21ecd874021081ff1205351bde2db22a06
Release:	1%{?dist}
Summary:	library and utilities to manipulate mac dmg disk images

Group:		
License:	GPL	
URL:		https://github.com/planetbeing/libdmg-hfsplus

BuildRequires: git,cmake	
Requires:      zlib,openssl	

%description
foo

%prep
git clone https://github.com/planetbeing/libdmg-hfsplus
git reset --hard %{version}


%build
cmake -DCMAKE_INSTALL_PREFIX=%{_bindir} CMakeLists.txt
make

%install
make install

%files
%{_bindir}/dmg
%{_bindir}/hfsplus
%{_bindir}/hdutil

%changelog

