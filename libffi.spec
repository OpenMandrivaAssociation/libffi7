# libffi is used by glib2.0, which in turn is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 7
%define libname %mklibname ffi %{major}
%define lib32name libffi%{major}

# (tpg) optimize it a bit
%global optflags %optflags -O3

Summary:	Old version of a portable foreign function interface library
Name:		libffi7
Version:	3.3
Release:	4
Group:		System/Libraries
License:	BSD
Url:		https://sourceware.org/libffi
Source0:	ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
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

%prep
%autosetup -p1 -n libffi-%{version}
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

# No -devel packages for compat packages
rm -rf %{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_libdir}/*.{a,so} \
%if %{with compat32}
	%{buildroot}%{_prefix}/lib/pkgconfig \
	%{buildroot}%{_prefix}/lib/*.{a,so} \
%endif
	%{buildroot}%{_includedir} \
	%{buildroot}%{_mandir}/man3 \
	%{buildroot}%{_infodir}

%files -n %{libname}
%{_libdir}/libffi.so.%{major}*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libffi.so.%{major}*
%endif
