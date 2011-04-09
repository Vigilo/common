%define module  @SHORT_NAME@

Name:       vigilo-%{module}
Summary:    @SUMMARY@
Version:    @VERSION@
Release:    1%{?svn}%{?dist}
Source0:    %{name}-%{version}.tar.gz
URL:        @URL@
Group:      System/Servers
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-build
License:    GPLv2
Buildarch:  noarch

BuildRequires:   python-distribute
BuildRequires:   python-babel

Requires:   python-babel >= 0.9.4
Requires:   python-distribute
Requires:   python-configobj


%description
@DESCRIPTION@
This library is part of the Vigilo Project <http://vigilo-project.org>

%prep
%setup -q

%build
make PYTHON=%{__python}

%install
rm -rf $RPM_BUILD_ROOT
make install \
    DESTDIR=$RPM_BUILD_ROOT \
    PREFIX=%{_prefix} \
    PYTHON=%{__python}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*


%changelog
* Fri Jan 21 2011 Vincent Quéméner <vincent.quemener@c-s.fr> - 1.0-2
- Rebuild for RHEL6.

* Mon Feb 08 2010 Aurelien Bompard <aurelien.bompard@c-s.fr> - 1.0-1
- initial package
