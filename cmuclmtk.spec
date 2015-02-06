%define debug_package %{nil}

Summary: The CMU-Cambridge Statistical Language Modeling Toolkit
Name: cmuclmtk
Version: 0.7
Release: 2
License: GPL
Group: Development/Other
Source: http://downloads.sourceforge.net/project/cmusphinx/cmuclmtk/0.7/%{name}-%{version}.tar.gz
URL: http://cmusphinx.sourceforge.net/

%description
The CMU-Cambridge Statistical Language Modeling Toolkit need for make
cmu-sphinx's language models

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
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/%{name}/*
%doc README NEWS ChangeLog TODO


%changelog
* Thu Apr 28 2011 zamir <zamir@mandriva.org> 0.7-0mdv2011.0
+ Revision: 659876
- add autoconf
- new realease

* Thu Jan 06 2011 zamir <zamir@mandriva.org> 0.10753-1mdv2011.0
+ Revision: 629147
- added svn release number
- small fix spec file
- first build
- Created package structure for cmuclmtk.

