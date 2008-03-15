%define 	module	hgview
%define     snap    20080314
Summary:	GTK or Qt4 based replacement for hgk
Summary(pl.UTF-8):	Zastępca hgk bazujący na GTK albo Qt4
Name:		hgview
Version:	0.3.0
Release:	0.%{snap}
License:	GPL v2
Group:		Development/Version Control
Source0:	%{name}-%{snap}.tar.bz2
#Source0-md5:   5675a6728830d70a2a2b96040d6ec6ce
URL:		http://www.logilab.org/project/hgview
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
#%pyrequires_eq  python-libs
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A faster implementation of hgk using pygtk/pyqt4. Its primary purpose
was to be able to browse the linux kernel mercurial repository.

%description -l pl.UTF-8
Szybsza implementacja hgk z wykorzystaniem pygtk/pyqt4. Jej główną
funkcją była możliwość przeglądania repozytorium mercuriala jądra
linuxa.

%package common
Summary:	Common files of hgview
Summary(pl.UTF-8):	Pliki wspólne dla hgview
Group:		Development/Version Control
%pyrequires_eq	python-modules
Requires:	%{name}-GUI

%description common
Common files for hgview used by hgview-gtk and hgview-qt.

%description common -l pl.UTF-8
Wspólne pliki dla hgview używane przez hgview-gtk i hgview-qt.

%package gtk
Summary:	GTK GUI for hgview
Summary(pl.UTF-8):	GUI w GTK dla hgview
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Provides:	%{name}-GUI

%description gtk
GTK GUI for hgview.

%description gtk -l pl.UTF-8
GUI w GTK dla hgview.

%package qt
Summary:	Qt4 GUI for hgview
Summary(pl.UTF-8):	GUI w Qt4 dla hgview
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Provides:	%{name}-GUI

%description qt
Qt4 GUI for hgview.

%description qt -l pl.UTF-8
GUI w Qt4 dla hgview.

%prep
%setup -q -n %{module}-%{snap}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/hgview
%dir %{py_sitescriptdir}/hgview
%{py_sitescriptdir}/hgview/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info
%{_mandir}/man1/hgview.1*

%files gtk
%defattr(644,root,root,755)
%{_datadir}/hgview/hgview.glade
%{py_sitescriptdir}/hgview/gtk

%files qt
%defattr(644,root,root,755)
%{_datadir}/hgview/hgview.ui
%{py_sitescriptdir}/hgview/qt4
