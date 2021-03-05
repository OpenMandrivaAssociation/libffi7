# libffi is used by glib2.0, which in turn is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 7
%define libname %mklibname ffi %{major}
%define devname %mklibname -d ffi
%define staticname %mklibname -d -s ffi
%define lib32name libffi%{major}
%define dev32name libffi-devel
%define static32name libffi-static-devel

# (tpg) optimize it a bit
%global optflags %optflags -O3

Summary:	A portable foreign function interface library
Name:		libffi
Version:	3.3
Release:	3
Group:		System/Libraries
License:	BSD
Url:		http://sourceware.org/%{name}
Source0:	ftp://sourceware.org/pub/%{name}/%{name}-%{version}.tar.gz
Patch1:		libffi-3.2.1-o-tmpfile-eacces.patch
BuildRequires:	autoconf

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

%package -n %{libname}
Summary:	A portable foreign function interface library
Group:		System/Libraries

%description -n %{libname}
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

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	ffi-devel = %{EVRD}
Obsoletes:	%{mklibname -d ffi 5} < %{EVRD}

%description -n %{devname}
This package contains libraries and header files for developing
applications that use %{name}.

# The static libffi is used to link Host Dalvik while building
# Android from source - please don't remove it.
%package -n %{staticname}
Summary:	Static libraries for %{name}
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Provides:	ffi-static-devel = %{EVRD}

%description -n %{staticname}
This package contains static libraries for developing
applications that use %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	A portable foreign function interface library (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
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

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/C
Requires:	%{lib32name} = %{EVRD}
Requires:	%{devname} = %{EVRD}

%description -n %{dev32name}
This package contains libraries and header files for developing
applications that use %{name}.

%package -n %{static32name}
Summary:	Static libraries for %{name} (32-bit)
Group:		Development/C
Requires:	%{dev32name} = %{EVRD}

%description -n %{static32name}
This package contains static libraries for developing
applications that use %{name}.
%endif

%prep
%autosetup -p1
# Don't mess with CFLAGS, we know what we want
sed -i -e 's,AX_CC_MAXOPT,dnl AX_CC_MAXOPT,g' configure.ac
autoreconf -fiv
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32 --enable-static
cd ..
%endif
mkdir build
cd build
%configure --enable-static

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libffi.so.%{major}*

%files -n %{devname}
%doc LICENSE
%{_libdir}/pkgconfig/libffi.pc
%{_includedir}/ffi*.h
%{_libdir}/libffi.so
%{_mandir}/man3/*
%{_infodir}/libffi.info.*

%files -n %{staticname}
%{_libdir}/*.a

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libffi.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/pkgconfig/libffi.pc
%{_prefix}/lib/libffi.so

%files -n %{static32name}
%{_prefix}/lib/*.a
%endif
