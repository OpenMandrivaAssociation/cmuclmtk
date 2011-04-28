Summary: The CMU-Cambridge Statistical Language Modeling Toolkit
Name: cmuclmtk
Version: 0.7
Release: %mkrel 0
License: GPL
Group: Development/Other
Source: http://downloads.sourceforge.net/project/cmusphinx/cmuclmtk/0.7/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
URL: http://cmusphinx.sourceforge.net/

%description
The CMU-Cambridge Statistical Language Modeling Toolkit need for make cmu-sphinx's language models

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%make

%install
rm -fr %{buildroot}
%makeinstall_std

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/%{name}/*
%doc README NEWS ChangeLog TODO
