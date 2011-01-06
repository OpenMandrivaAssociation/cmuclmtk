%define svnrelease 10753

Summary: The CMU-Cambridge Statistical Language Modeling Toolkit
Name: cmuclmtk
Version: 0.%svnrelease
Release: %mkrel 1
License: GPL
Group: Development/Other
Source: http://cmusphinx.svn.sourceforge.net/viewvc/cmusphinx/trunk/cmuclmtk/cmusphinx-%{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
URL: http://cmusphinx.sourceforge.net/

%description
The CMU-Cambridge Statistical Language Modeling Toolkit need for make cmu-sphinx's language models

%prep
%setup -q -n %{name}

%build
./autogen.sh
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
%doc README ReleaseNotes
