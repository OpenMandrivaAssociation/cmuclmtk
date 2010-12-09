Summary:	The CMU-Cambridge Statistical Language Modeling Toolkit
Name:		cmuclmtk
Version:	svn1
Release:	%mkrel 1
License:	GPL
Group:		Development/Other
Source:		cmusphinx-%{name}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
The CMU-Cambridge Statistical Language Modeling Toolkit need for make cmu-sphinx's language models

%prep
%setup -q -n %{name}

%build
rm -fr %{buildroot}
./autogen.sh
%configure
%make

%install
%makeinstall_std

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/%{name}/*
%doc README ReleaseNotes
