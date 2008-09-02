%define major 5
%define libname %mklibname ffi %major
#gw: keep the major, as there's another libffi from gcc
%define develname %mklibname -d ffi %major
Name:		libffi
Version:	3.0.6
Release:	%mkrel 1
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

%package -n %libname
Summary:	A portable foreign function interface library
Group:		System/Libraries

%description -n %libname
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

%package -n %develname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Provides:	 libffi-devel = %version-%release
Provides:	 ffi5-devel = %version-%release
#gw gcc's libffi-devel will be renamed like this:
Conflicts:	 %mklibname -d ffi 4

%description -n %develname
This package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -q


%build
%configure2_5x --disable-static
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%clean
rm -rf $RPM_BUILD_ROOT


%if %mdvver < 200900
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%post -n %develname
%_install_info libffi.info

%preun -n %develname
%_remove_install_info libffi.info


%files -n %libname
%defattr(-,root,root,-)
%doc LICENSE README
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}-%{version}
%{_libdir}/*.so
%{_mandir}/man3/*
%{_infodir}/libffi.info.*

