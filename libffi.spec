%define major		5
%define libffi		%mklibname ffi %{major}
%define libffi_devel	%mklibname -d ffi

Name:		libffi
Version:	3.0.10
Release:	2
Summary:	A portable foreign function interface library
Group:		System/Libraries
License:	BSD
URL:		http://sourceware.org/libffi
Source0:	ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Compilers for high level languages generate code that follow certain
conventions.  These conventions are necessary, in part, for separate
compilation to work.  One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function.  A
calling convention also specifies where the return value for a function
is found.  

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function.  `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface.  A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language.  The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface.  A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.  

%package	-n %{libffi}
Summary:	A portable foreign function interface library
Group:		System/Libraries

%description	-n %{libffi}
Compilers for high level languages generate code that follow certain
conventions.  These conventions are necessary, in part, for separate
compilation to work.  One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function.  A
calling convention also specifies where the return value for a function
is found.  

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function.  `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface.  A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language.  The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface.  A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.

%package	-n %{libffi_devel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libffi} = %{EVRD}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Provides:	libffi-devel = %{EVRD}
Provides:	ffi5-devel = %{EVRD}
Provides:	ffi-devel = %{EVRD}
Obsoletes:	%{mklibname -d ffi 5}

%description	-n %{libffi_devel}
This package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -q


%build
%configure2_5x --disable-static
%make


%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%if %mdvver < 200900
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%post		-n %{libffi_devel}
%_install_info libffi.info

%preun		-n %{libffi_devel}
%_remove_install_info libffi.info


%files -n	%{libffi}
%defattr(-,root,root,-)
%doc LICENSE README
%{_libdir}/*.so.%{major}*

%files		-n %{libffi_devel}
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}-%{version}
%{_libdir}/*.so
%{_mandir}/man3/*
%{_infodir}/libffi.info.*

