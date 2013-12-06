%define major 6
%define libname %mklibname ffi %{major}
%define devname %mklibname -d ffi

Summary:	A portable foreign function interface library
Name:		libffi
Version:	3.0.13
Release:	5
Group:		System/Libraries
License:	BSD
Url:		http://sourceware.org/%{name}
Source0:	ftp://sourceware.org/pub/%{name}/%{name}-%{version}.tar.gz

%track
prog %{name} = {
	url = http://sourceware.org/%{name}
	regex = "libffi-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Compilers for high level languages generate code that follow certain
conventions. These conventions are necessary, in part, for separate
compilation to work. One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function. A
calling convention also specifies where the return value for a function
is found.

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function. `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface. A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language. The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface. A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.

%package -n	%{libname}
Summary:	A portable foreign function interface library
Group:		System/Libraries

%description -n	%{libname}
Compilers for high level languages generate code that follow certain
conventions. These conventions are necessary, in part, for separate
compilation to work. One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function. A
calling convention also specifies where the return value for a function
is found.

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function. `Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The `libffi' library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface. A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language. The
`libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface. A layer must
exist above `libffi' that handles type conversions for values passed
between the two languages.


%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	ffi-devel = %{EVRD}
Obsoletes:	%{mklibname -d ffi 5} < %{EVRD}

%description -n %{devname}
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libffi.so.%{major}*

%files -n %{devname}
%doc LICENSE README
%{_libdir}/pkgconfig/libffi.pc
%{_libdir}/%{name}-%{version}
%{_libdir}/libffi.so
%{_mandir}/man3/*
%{_infodir}/libffi.info.*

