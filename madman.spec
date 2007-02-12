Summary:	Madman Administrates Digital Music Archives Neatly
Summary(pl.UTF-8):   Madman - miłe administrowanie archiwami cyfrowej muzyki
Name:		madman
Version:	0.93
Release:	0.1
License:	CHECK FIRST!
Group:		Productivity/Multimedia/Sound/Utilities
Source0:	http://dl.sourceforge.net/madman/%{name}-%{version}.tar.gz
# Source0-md5:	a9aeef95248ecd55e0479a6b8dec43f2
#Source1:	%{name}.desktop
#Source1:	kdissert-kde.py
URL:		http://madman.sourceforge.net/
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libid3tag-devel >= 0.15.1b
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	qt-devel >= 6:3.1
BuildRequires:	scons
BuildRequires:	xmms-devel >= 2:1.2.6
#BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Madman is a music manager application that allows you to easily keep
your music database organized and tidy, and it helps you listen to
better music, be happier, brighten your teeth and quickly restore
world peace.

%description -l pl.UTF-8
Madman (Madman Administrates Digital Music Archives Neatly) to
aplikacja do zarządzania muzyką pozwalająca łatwo utrzymywać w
porządku bazę danych muzyki i pomagająca w słuchaniu lepszej muzyki,
byciu szczęśliwszym, wybieleniu zębów i szybkiemu przywróceniu
pokoju na świecie.

%prep
%setup -q
#install %{SOURCE1} ./kde.py

%build
export CXXFLAGS="%{rpmcflags}"
export QTDIR="%{_usr}"
# autodetects all needed paths from kde-config not sure it supports amd64 at the moment
# im talking about it with the maintainer of kde's scons-based buildsystem

scons configure \
	qtincludes=%{_includedir}/qt \
	prefix=%{_prefix} %{?debug:debug=full} \
%if "%{_lib}" == "lib64"
	libsuffix=64 \
%endif
	qtlibs=%{_libdir}
scons

#cp -f /usr/share/automake/config.sub admin
#export PATH=/usr/share/unsermake:$PATH
#%{__make} -f admin/Makefile.common cvs

#export QTDIR=/usr
#scons prefix=%{_prefix} qt_directory=/usr/include/qt
#
#%configure \
#%if "%{_lib}" == "lib64"
#	--enable-libsuffix=64 \
#%endif
#	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
#	--with-qt-libraries=%{_libdir}
#%{__make}

%install
rm -rf $RPM_BUILD_ROOT

scons prefix=$RPM_BUILD_ROOT%{_prefix} install

#install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
#
#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT \
#	kde_htmldir=%{_kdedocdir} \
#	kde_libs_htmldir=%{_kdedocdir} \
#	kdelnkdir=%{_desktopdir} \

# move the .desktop file to desktopdir
#mv $RPM_BUILD_ROOT{%{_datadir}/applnk/*/*.desktop,%{_desktopdir}}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
%{_kdedocdir}/*
